from sys import*
from select import*
from socket import*
serv_addrss=("127.0.0.1",8001)
fd=socket(AF_INET,SOCK_STREAM)
fd.connect(serv_addrss)
while True:			
	fd.send(raw_input())
	rec=fd.recvfrom(1000)
	print rec[0]
fd.close()
	
