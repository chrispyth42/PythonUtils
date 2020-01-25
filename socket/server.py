import socket

#Create the socket object with IPv4, in streaming mode
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind it to localhost, port 4444
s.bind(('', 4444))

#Listen with a queue of 5
s.listen(5)

while 1:
    #When a connection is made, store the client socket, and client address in those variables
    clientsocket, address = s.accept()
    print("Connected from: " + str(address))

    #Send the client socket a utf-8 bytestring
    clientsocket.send(bytes("Python message!","utf-8"))

#Tutorial video this is from:
#https://youtu.be/Lbfe3-v7yE0
