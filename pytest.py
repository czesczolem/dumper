import subprocess
import requests
import json
import time
import os
import signal
from threading import Thread

def get_state(delay):
	try:
		time.sleep(delay)
		r = requests.get('http://0.0.0.0:5050/tcp_flag')
		json_data = json.loads(r.text)
		tcp_flag = json_data["tcp_flag"]
		print "[Client] Flag Check!"
		return tcp_flag
	except Exception, e:
		print "[Server Error] Can't connect with server"

if __name__ == '__main__':

	while True:
		tcp_flag = get_state(5)
		if tcp_flag == True:
			filename = time.time()
			dump_time_limit = "5000"
			command = "timeout {} tcpdump > {}.txt".format(dump_time_limit, filename)
			p = subprocess.Popen(command, shell=True)
			while True:
				tcp_flag = get_state(1)
				print "[Client] Dumping!"
				if tcp_flag == False:
					kill_tcpdump_command = "kill $(ps aux | grep tcpdump | awk '{print $2}')"
					subprocess.call(kill_tcpdump_command, shell=True)
					print "[Client] Dumping is over"
					break






