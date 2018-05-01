import socket
COMMANDS_PORT = 5640
RPi_HOST = "10.0.0.12"
addr = socket.getaddrinfo(RPi_HOST, COMMANDS_PORT)[0][-1]
s = socket.socket()
print("Connecting to RPi: ", addr)
s.connect(addr)
s.send("Ready")
