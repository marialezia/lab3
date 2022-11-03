#invio di un array, client
import socket, pickle

HOST = 'localhost'
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
arr = ([1,2,3,4,5,6], [7,8,9,10,11,12])
data_string = pickle.dumps(arr) #converte array in stringa
s.send(data_string)

data = s.recv(4096)
print(data.decode())

s.close()

