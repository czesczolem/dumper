import sys
import os
import requests
import json

if __name__ == '__main__':

	r = requests.get('http://0.0.0.0:5050/tcp_flag')
	json_data = json.loads(r.text)
	tcp_flag = json_data["tcp_flag"]
	print tcp_flag

	#TODO: subprocess

	if tcp_flag == True:
		command = "echo test > test.txt"
		os.system(command)
		sys.exit(0)
	else:
		sys.exit(0)

