# server.py 
import socket                                         
import time

PORT = 5640                                         

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

#Get own IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
local_ip_address = s.getsockname()[0]

# bind to the port
serversocket.bind(('', PORT))     
print("Host IP:", local_ip_address, " listening on port: ", PORT)
print("Waiting for connection")                             

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()      

    print("Got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()