#invio di una stringa, client

import socket

host = 'local host'
print("host ", host)



port = 12345                   

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall('Hello, world'.encode())

data = s.recv(1024)
print("server replied: ", data.decode())
s.close()

