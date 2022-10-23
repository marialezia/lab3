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

y = np.ones(len(registrazione))
for i in range(len(registrazione)):
    y[i] = registrazione[i][0]
    

HOST = ''
PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

for i in range(len(registrazione)):
    yb = st.pack('d', y[i])
    s.send(yb)

s.close()

