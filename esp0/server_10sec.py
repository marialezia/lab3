import socket
import numpy as np
import matplotlib.pyplot as plt
import struct as st
import soundcard as sc

HOST = ''
PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)
y = np.empty(0)

for i in range(480000):
    data = conn.recv(8)
    dd = st.unpack('d',data)
    y = np.append(y, dd)
    if not data: break

print('array acquisito è lungo ', len(y))
print('array acquisito: ', y)
conn.close()


speakers = sc.all_speakers()
print("Speaker disponibili: ", speakers, "\n")
default_speaker = sc.default_speaker()
print("Speaker selezionato: ", default_speaker, "\n")


print("\n")
default_speaker.play(y/np.max(y), samplerate=48000)
print("L'array dei dati registrati è lungo ", len(y))



t = 1/48000
x = np.arange(0, 10, t)

plt.title('audio')
plt.plot(x, y, color = 'green')
plt.show()
