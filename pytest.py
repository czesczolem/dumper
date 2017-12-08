import sys
import os

with open('/var/tcp_dump/test', 'r') as f:
	data = f.read()
print data
if data != "0":
    with open('/var/tcp_dump/test', 'w') as f:
    	f.write("0")
	command = "sudo timeout 100 tcpdump >> /var/tcp_dump/tcptest"
	os.system(command)
	sys.exit(0)
else:
	sys.exit(0)

