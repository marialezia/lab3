#client 1 secondo

import socket
import struct as st
import soundcard as sc
import numpy as np

mics = sc.all_microphones()
print("Microfoni disponibili: ", mics, "\n")
default_mic = sc.default_microphone()
print("Microfono selezionato: ", default_mic, "\n")
registrazione = default_mic.record(samplerate=48000, numframes=48000)
print("Array acquisito: ")
print(registrazione)

l = len(registrazione)
y = np.ones(l)
for i in range(l):
    y[i] = registrazione[i][0]
    

HOST = ''
PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

lb = st.pack('i', l)
s.send(lb)

for i in range(l):
    yb = st.pack('d', y[i])
    s.send(yb)

s.close()
