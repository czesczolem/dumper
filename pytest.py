import subprocess
import requests
import json
import time


# TODO:
# parallel,  max workers
# site with link list
# tcp dump rebuild nie sluchac z jakiegos tam plus arpy wyjebac

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

	session_start_time = 0

	while True:
		tcp_flag = get_state(5)
		if tcp_flag == True:
			filename = get_filename()
			file_path = 'dumps/' + filename
			dump_time_limit = 5
			session_start_time = time.time()
			tcp_dump_command = "tcpdump -i any -s 0 -tttt -XX -w"
			command = "timeout {} {} {}.pcap".format(dump_time_limit, tcp_dump_command, file_path)
			p = subprocess.Popen(command, shell=True)
			while True:
				tcp_flag = get_state(1)
				print "[Client] Dumping!"
				session_time = int(time.time() - session_start_time)
				if tcp_flag == False:
					kill_tcpdump_command = "kill $(ps aux | grep " + filename + " | awk '{print $2}')"
					subprocess.call(kill_tcpdump_command, shell=True)
					print "[Client] Dumping is over"
					break
				elif session_time > dump_time_limit:
					requests.post('http://0.0.0.0:5050/tcp_flag')
					print "session_time > dump_time_limit ", session_time
					break






