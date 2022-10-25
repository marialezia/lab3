#invio di una stringa, server

import socket

host = ''        
port = 12345     
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print( "host " ,host, " porta ", port)

s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    try:
        data = conn.recv(1024)

        if not data: break

        print( "Client Says: ", data.decode())
        
        conn.sendall("Recieved".encode())

    except socket.error:
        print("Error Occured.")
        break

conn.close()
