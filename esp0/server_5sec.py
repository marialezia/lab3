#server 5 secondi

import socket
import time
import numpy as np
import matplotlib.pyplot as plt
import struct as st
import soundcard as sc

HOST = ''
PORT = 12355
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)

lb = st.unpack('i', conn.recv(4) )

l = int(lb[0])

print('array da acquisire è lungo ', l)

y = np.ones(l)

for i in range(l):
    data = conn.recv(8)
    print(i, len(data))
    time.sleep(0.00001)
    dd = st.unpack('d',data)
    y[i] = float(dd[0])
    if not data: break

print('array acquisito: ', y)

conn.sendall("audio ricevuto ".encode())

conn.close()


speakers = sc.all_speakers()
print("Speaker disponibili: ", speakers, "\n")
default_speaker = sc.default_speaker()
print("Speaker selezionato: ", default_speaker, "\n")


print("\n")
default_speaker.play(y/np.max(y), samplerate=48000)
print("L'array dei dati registrati è lungo ", len(y))


t = 5/l
x = np.arange(0, 5, t)

plt.title('Audio 5 secondi')
plt.plot(x, y, color = 'violet')
plt.xlabel('Tempo[s]')
plt.ylabel('Intensità segnale')
plt.show()

