import subprocess
import requests
import json
import time
from threading import Thread

def get_state(delay):
	try:
		time.sleep(delay)
		r = requests.get('http://0.0.0.0:5050/tcp_flag')
		json_data = json.loads(r.text)
		tcp_flag = json_data["tcp_flag"]
		print "[Server] Connected!"
		return tcp_flag
	except Exception, e:
		print "[Server Error] Can't connect with server"

if __name__ == '__main__':

	while True:
		tcp_flag = get_state(5)
		if tcp_flag == True:
			filename = "test"
			dump_time = "5"
			command = "timeout {} echo test > {}.txt".format(dump_time, filename)
			p = subprocess.Popen(command, shell=True)
			while True:
				tcp_flag = get_state(5)
				if tcp_flag == False:
					p.kill()

			# requests.post('http://0.0.0.0:5050/tcp_flag')






