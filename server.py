from sys import*
from select import*
from socket import*
serv_addrss=("127.0.0.1",8001)
fd=socket(AF_INET,SOCK_STREAM)
fd.bind(serv_addrss)
fd.listen(5)
print "Listening................."
client=fd.accept()
while True:
	rec=client[0].recvfrom(1000)
	print rec[0]
	client[0].send(raw_input())
fd.close()
	
