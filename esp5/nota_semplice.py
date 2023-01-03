import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants, fft
import sys, os
import funzioni as fz



#apro il file .wav
data, samplerate = sf.read('pulita_semplice.wav')


print('samplerate = ', samplerate)
print('data = ', data)
print('lunghezza = ', len(data))


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
print('lunghezza trasformata fourier = ', datafft.size)
print('lunghezza array dati = ', len(y))

fftfreq = fft.rfftfreq(len(y), 1.0/samplerate)

print('trasformata di Fourier = ', datafft)
print('lunghezza tf = ', len(datafft))
print('frequenze tf = ', fftfreq)
print('lunghezza frequenze = ', len(fftfreq))


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
'''
plt.plot(fftfreq, p, color='limegreen')
plt.xlabel('Frequenza (hz)')
plt.ylabel('Potenza (u.a)')
plt.show()
'''

#trovo la posizione dei massimi
sogliaa = 100000
maxx = fz.massimi(p, sogliaa,14)
'''
plt.plot(fftfreq, p,'-o', markersize = 1, color='limegreen')
for i in range(len(maxx)):
    plt.plot(fftfreq[maxx[i]], p[maxx[i]],'o', color = 'forestgreen', markersize = 4)
plt.xlabel('Frequenza (hz)')
plt.ylabel('Potenza (u.a)')
plt.show()
'''


fz.printaFreq(fftfreq, maxx)
#mascherare (mettere a zero) i coefficienti, tranne alcuni scelti
#creo maschera

mask = fz.mascheraCoeff(p, maxx, 2000000, 3)

plt.plot(fftfreq, p,'-o', markersize = 1, color='limegreen')
plt.plot(fftfreq[mask], p[mask], 'o', color = 'forestgreen', markersize = 4)
plt.show()
