import soundcard as sc
import socket, pickle
import numpy as np
import matplotlib.pyplot as plt

mics = sc.all_microphones()
print("Microfoni disponibili: ", mics, "\n")
default_mic = sc.default_microphone()
print("Microfono selezionato: ", default_mic, "\n")
audio = default_mic.record(samplerate=48000, numframes=48000)
print("Array acquisito: ")
print(audio)
print("\n")

el = np.ones(len(audio))
for i in range(len(audio)):
    el[i]  = data[i][0]

HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


for i in range(4):
    data_string = pickle.dumps(el[i])
    s.send(data_string)
data = s.recv(4)
data_arr = pickle.loads(data)

s.close()

print ('Received', repr(data_arr))

