import subprocess
import requests
import json
import time

def get_state(delay):
	try:
		time.sleep(delay)
		r = requests.get('http://0.0.0.0:5050/tcp_flag')
		json_data = json.loads(r.text)
		tcp_flag = json_data["tcp_flag"]
		print "[Client] Flag Check: ", tcp_flag
		return tcp_flag

	except Exception:
		print "[Server Error] Can't connect with server"
		return None

def get_filename():
	try:
		r = requests.get('http://0.0.0.0:5050/filename')
		json_data = json.loads(r.text)
		filename = json_data["filename"]
		print "set filename: ", filename
		return filename

	except Exception:
		print "[Server Error] Can't find file"

if __name__ == '__main__':

	while True:
		tcp_flag = get_state(5)
		if tcp_flag == True:
			filename = get_filename()
			dump_time_limit = "5000"
			tcp_dump_command = "tcpdump -i any -s 0 -tttt -XX -w"
			command = "timeout {} {} {}.pcap".format(dump_time_limit, tcp_dump_command, filename)
			p = subprocess.Popen(command, shell=True)
			while True:
				tcp_flag = get_state(1)
				print "[Client] Dumping!"
				if tcp_flag == False:
					#TODO:
					#tcp kill by filename
					#change flag after 5 mins
					kill_tcpdump_command = "kill $(ps aux | grep tcpdump | awk '{print $2}')"
					subprocess.call(kill_tcpdump_command, shell=True)
					print "[Client] Dumping is over"
					break






