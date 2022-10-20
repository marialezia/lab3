import soundcard as sc
import socket
import numpy as np
import matplotlib.pyplot as plt

HOST = ''
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)

while 1:
    data = conn.recv(4096)
    if not data: break
    conn.send(data)
conn.close()

speakers = sc.all_speakers()
print("Speaker disponibili: ", speakers, "\n")
default_speaker = sc.default_speaker()
default_speaker.play(data/np.max(data), samplerate=48000)
print("L'array dei dati registrati è lungo ", len(data))

y = np.ones(len(data))
for i in range(len(data)):
    y[i]  = data[i][0]

t = 1/48000
x = np.arange(0, 10, t)

plt.title('audio')
plt.plot(x, y, color = 'red')
plt.show()

