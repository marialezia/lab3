#invio di un array, server
import socket
import pickle

HOST = 'localhost'
PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)

data = conn.recv(4096)

data_arr = pickle.loads(data)
print('array ricevuto: ', data_arr)

if not data_arr:
	conn.sendall('non Ricevuto'.encode())
else:
	conn.sendall('Ricevuto'.encode()) 

conn.close()
