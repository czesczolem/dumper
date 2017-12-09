import sys
import os
import subprocess
import requests
import json
import time

if __name__ == '__main__':
	while True:
		try:
			time.sleep(5)
			r = requests.get('http://0.0.0.0:5050/tcp_flag')
			json_data = json.loads(r.text)
			tcp_flag = json_data["tcp_flag"]
			print "Connected with server"
			print "tcp_flag: ", tcp_flag

			#TODO:
			#subprocess

			if tcp_flag == True:
				filename = "test.txt"
				dump_time = "5"
				command = "timeout {} tcpdump > {}".format(dump_time, filename)
				subprocess.call(command, shell=True)
				requests.post('http://0.0.0.0:5050/tcp_flag')
			# Cron
			# 	sys.exit(0)
			# else:
			# 	sys.exit(0)
		except Exception, e:
			print "[Server Error] Can't connect with server"


