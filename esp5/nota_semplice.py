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

#printo frequenze
fz.printaFreq(fftfreq, maxx)

#selezionare i picchi, vari casi:

#1) il picco principale
maskpp = fz.mascheraCoeff(p, maxx, 7000000, 0)

'''
plt.plot(fftfreq, p,'-o', markersize = 1, color='limegreen')
plt.plot(fftfreq[maskpp], p[maskpp], 'o')
plt.show()
'''

#2) i primi due picchi principali, ma solo il termine "centrale"
maskpp2 = fz.mascheraCoeff(p, maxx, 5000000, 0)

'''
plt.plot(fftfreq, p,'-o', markersize = 1, color='limegreen')
plt.plot(fftfreq[maskpp2], p[maskpp2], 'o')
plt.show()
'''

#3) i picchi principali, ma solo il termine "centrale"
maskpp3 = fz.mascheraCoeff(p, maxx, 2000000, 0)

'''
plt.plot(fftfreq, p,'-o', markersize = 1, color='limegreen')
plt.plot(fftfreq[maskpp3], p[maskpp3], 'o')
plt.show()
'''

#4) i picchi principali con anche 1 o 2 termini, per lato, oltre quello centrale
maskpp4 = fz.mascheraCoeff(p, maxx, 2000000, 3)
'''
plt.plot(fftfreq, p,'-o', markersize = 1, color='limegreen')
plt.plot(fftfreq[maskpp4], p[maskpp4], 'o')
plt.show()
'''

'''
plt.plot(fftfreq, p,'-o', markersize = 1, color='limegreen')
for i in range(len(maxx)):
    plt.plot(fftfreq[maxx[i]], p[maxx[i]],'o', color = 'forestgreen', markersize = 4)
plt.xlabel('Frequenza (hz)')
plt.ylabel('Potenza (u.a)')
plt.show()
'''


#dati filtrati
filtropp = datafft.copy()
filtropp[~ maskpp]=0

filtropp2 = datafft.copy()
filtropp2[~ maskpp2]=0

filtropp3 = datafft.copy()
filtropp3[~ maskpp3]=0

filtropp4 = datafft.copy()
filtropp4[~ maskpp4]=0

#risintetizziamo i dati filtrati
dataSint1 = fft.irfft(filtropp, n = len(y))
dataSint2 = fft.irfft(filtropp2, n = len(y))
dataSint3 = fft.irfft(filtropp3, n = len(y))
dataSint4 = fft.irfft(filtropp4, n = len(y))

#produco file audio
                       
sf.write('notaSempliceDataSint1.wav', dataSint1, samplerate)
sf.write('notaSempliceDataSint2.wav', dataSint2, samplerate)
sf.write('notaSempliceDataSint3.wav', dataSint3, samplerate)
sf.write('notaSempliceDataSint4.wav', dataSint4, samplerate)

#grafico waveform
fig,ax = plt.subplots(2,2, figsize=(12,12) )
ax[0][0].set_title('picco principale')
ax[0][1].set_title( 'primi due picchi principali')
ax[1][0].set_title('picchi principali solo termine centrale')
ax[1][1].set_title('picchi principali con un termine ai lati')


ax[0][0].plot(x, y, color = 'seagreen', alpha = 0.5)
ax[0][1].plot(x, y, color = 'seagreen', alpha = 0.5)
ax[1][0].plot(x, y, color = 'seagreen', alpha = 0.5)
ax[1][1].plot(x, y, color = 'seagreen', alpha = 0.5)

ax[0][0].plot(x, dataSint1, alpha = 0.5, label = 'picco principale')
ax[0][1].plot(x, dataSint2, alpha = 0.5, label = 'primi due picchi principali')
ax[1][0].plot(x, dataSint3, alpha = 0.5, label = 'picchi principali solo termine centrale')
ax[1][1].plot(x, dataSint4, alpha = 0.5, label = 'picchi principali con un termine ai lati')
plt.legend()
plt.xlabel('Tempo[s]')
plt.ylabel('Ampiezza (u.a)')
plt.show()
