#client 5 secondi

import socket
import struct as st
import soundcard as sc
import numpy as np

mics = sc.all_microphones()
print("Microfoni disponibili: ", mics, "\n")
default_mic = sc.default_microphone()
print("Microfono selezionato: ", default_mic, "\n")
registrazione = default_mic.record(samplerate=48000, numframes=240000)
print("Array acquisito: ")
print(registrazione)

l = len(registrazione)
y = np.ones(l)
for i in range(l):
    y[i] = registrazione[i][0]

HOST = 'localhost'
#HOST = '192.168.4.33'
#HOST = '172.22.14.152'
PORT = 12355
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

lb = st.pack('i', l)
s.send(lb)

for i in range(l):
    yb = st.pack('d', y[i])
    s.send(yb)

    
data = s.recv(1024)
print('server replied: ', data.decode())

s.close()

