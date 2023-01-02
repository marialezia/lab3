import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants, fft

#apro il file .wav
data, samplerate = sf.read('pulita_semplice.wav')

print(samplerate)
print(data)
print(len(data))

#plotto la waveform
y = np.ones(len(data))
for i in range(len(data)):
    y[i]  = data[i][0]

t = 1/samplerate
durata = len(y)/samplerate
x = np.arange(0, durata, t)
'''
plt.title('Waveform nota pulita semplice')
plt.plot(x, y, color = 'darkturquoise')
plt.xlabel('Tempo[s]')
plt.ylabel('Ampiezza (u.a)')
plt.show()
'''
#creo un nuovo file .wav uguale al primo
#sf.write('pulita_semplice_recreated.wav', data, samplerate)

#fft dell'array
datafft = fft.rfft(y)
print(datafft.size)
print(len(y))

fftfreq = fft.rfftfreq(len(y), 1.0/samplerate)

print(datafft)
print(len(datafft))
print(fftfreq)
print(len(fftfreq))

#grafico ampiezze reale e immaginaria
'''
fig, ax = plt.subplots(2,1, figsize=(40,40))
ax[0].plot(fftfreq, datafft.real, color='rebeccapurple')
ax[1].plot(fftfreq, datafft.imag, color='cyan')
ax[0].set_title('Ampiezza reale')
ax[1].set_title('Ampiezza immaginaria')
fig.suptitle('fft')
plt.show()
'''
#potenza
p=np.absolute(datafft)**2

plt.plot(fftfreq, p, color='limegreen')
plt.xlabel('Frequenza (hz)')
plt.ylabel('Potenza (u.a)')
plt.show()
