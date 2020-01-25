import socket

#Create socket (IPv4 streaming mode), and connect to server raspberry pi
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("serverpi.local",4444))

#Recieve with a buffer of 1024 bytes (this will vary with message size)
msg = s.recv(1024)

#Print the recieved decoded message
print(msg.decode("utf-8"))