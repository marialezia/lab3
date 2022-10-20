import socket

host = socket.gethostname()
print("host ", host)
#host = "local host"
#host = "93.33.51.172"

port = 12345                   # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall('Hello, world'.encode())

data = s.recv(1024)
print("server replied: ", data.decode())
s.close()

