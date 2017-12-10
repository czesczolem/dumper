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
			filename = "test.txt"
			dump_time = "5"
			command = "timeout {} tcpdump > {}".format(dump_time, filename)
			subprocess.call(command, shell=True)
			requests.post('http://0.0.0.0:5050/tcp_flag')






