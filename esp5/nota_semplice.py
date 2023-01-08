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
ax[0].set_xlabel('Frequenza (Hz)')
ax[0].set_ylabel('Ampiezza reale (u.a.)')
ax[1].set_xlabel('Frequenza (Hz)')
ax[1].set_ylabel('Ampiezza immaginaria (u.a.)')
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
print(fftfreq[maskpp3])

'''
plt.plot(fftfreq, p,'-o', markersize = 1, color='limegreen')
plt.plot(fftfreq[maskpp3], p[maskpp3], 'o')
plt.show()
'''

#4) i picchi principali con anche 1 o 2 termini, per lato, oltre quello centrale
maskpp4 = fz.mascheraCoeff(p, maxx, 2000000, 5)
'''
plt.plot(fftfreq, p,'-o', markersize = 1, color='limegreen')
plt.plot(fftfreq[maskpp4], p[maskpp4], 'o')
plt.show()
'''


#5) i primi 3 picchi principali, ma solo il termine "centrale"
maskpp5 = fz.mascheraCoeff(p, maxx, 4400000, 0)

'''
plt.plot(fftfreq, p,'-o', markersize = 1, color='limegreen')
plt.plot(fftfreq[maskpp5], p[maskpp5], 'o')
plt.show()
'''
#6) i primi 4 picchi principali, ma solo il termine "centrale"
maskpp6 = fz.mascheraCoeff(p, maxx, 4000000, 0)

'''
plt.plot(fftfreq, p,'-o', markersize = 1, color='limegreen')
plt.plot(fftfreq[maskpp6], p[maskpp6], 'o')
plt.show()
'''
#7) i primi 5 picchi principali, ma solo il termine "centrale"
maskpp7 = fz.mascheraCoeff(p, maxx, 3400000, 0)

'''
plt.plot(fftfreq, p,'-o', markersize = 1, color='limegreen')
plt.plot(fftfreq[maskpp7], p[maskpp7], 'o')
plt.show()
'''
#8) i primi 6 picchi principali, ma solo il termine "centrale"
maskpp8 = fz.mascheraCoeff(p, maxx, 2660000, 0)
'''
plt.plot(fftfreq, p,'-o', markersize = 1, color='limegreen')
plt.plot(fftfreq[maskpp8], p[maskpp8], 'o')
plt.show()
'''

#8) i primi 7 picchi principali, ma solo il termine "centrale"
maskpp9 = fz.mascheraCoeff(p, maxx, 2400000, 0)
'''
plt.plot(fftfreq, p,'-o', markersize = 1, color='limegreen')
plt.plot(fftfreq[maskpp9], p[maskpp9], 'o')
plt.show()
'''

#4) i picchi principali con anche 1 o 2 termini, per lato, oltre quello centrale
maskpp0t = maskpp3
maskpp1t = fz.mascheraCoeff(p, maxx, 2000000, 2)
maskpp2t = fz.mascheraCoeff(p, maxx, 2000000, 3)
maskpp3t = fz.mascheraCoeff(p, maxx, 2000000, 4)
maskpp4t = fz.mascheraCoeff(p, maxx, 2000000, 5)
maskpp5t = fz.mascheraCoeff(p, maxx, 2000000, 6)


potPp0t = p.copy()
potPp0t[~ maskpp0t]=0

potPp1t = p.copy()
potPp1t[~ maskpp0t]=0

potPp2t = p.copy()
potPp2t[~ maskpp2t]=0

potPp3t = p.copy()
potPp3t[~ maskpp3t]=0

potPp4t = p.copy()
potPp4t[~ maskpp4t]=0

potPp5t = p.copy()
potPp5t[~ maskpp5t]=0


filtropp0t =  datafft.copy()
filtropp0t[~ maskpp0t]=0

filtropp1t =  datafft.copy()
filtropp1t[~ maskpp1t]=0

filtropp2t =  datafft.copy()
filtropp2t[~ maskpp2t]=0

filtropp3t =  datafft.copy()
filtropp3t[~ maskpp3t]=0

filtropp4t =  datafft.copy()
filtropp4t[~ maskpp4t]=0

filtropp5t =  datafft.copy()
filtropp5t[~ maskpp5t]=0

'''
fig3, ax3 = plt.subplots(1,3, figsize=(40,40))
for i in range(3):
    ax3[i].plot(fftfreq, p,'-o', color='limegreen')
ax3[0].set_title('Primo picco')
ax3[1].set_title('Secondo picco')
ax3[2].set_title('Terzo picco')
plt.show()
'''

plt.plot(fftfreq, p,'-o', markersize = 1, color='limegreen')
for i in range(len(maxx)):
    plt.plot(fftfreq[maxx[i]], p[maxx[i]],'o', color = 'forestgreen', markersize = 4)
plt.xlabel('Frequenza (hz)')
plt.ylabel('Potenza (u.a)')
plt.show()



#potenze filtrate
potPp = p.copy()
potPp[~ maskpp]=0

potPp2 = p.copy()
potPp2[~ maskpp2]=0

potPp3 = p.copy()
potPp3[~ maskpp3]=0

potPp4 = p.copy()
potPp4[~ maskpp4]=0

potPp5 = p.copy()
potPp5[~ maskpp5]=0

potPp6 = p.copy()
potPp6[~ maskpp6]=0

potPp7 = p.copy()
potPp7[~ maskpp7]=0

potPp8 = p.copy()
potPp8[~ maskpp8]=0

potPp9 = p.copy()
potPp9[~ maskpp9]=0

#dati filtrati
filtropp = datafft.copy()
filtropp[~ maskpp]=0

filtropp2 = datafft.copy()
filtropp2[~ maskpp2]=0

filtropp3 = datafft.copy()
filtropp3[~ maskpp3]=0

filtropp4 = datafft.copy()
filtropp4[~ maskpp4]=0

filtropp5 = datafft.copy()
filtropp5[~ maskpp5]=0

filtropp6 = datafft.copy()
filtropp6[~ maskpp6]=0

filtropp7 = datafft.copy()
filtropp7[~ maskpp7]=0

filtropp8 = datafft.copy()
filtropp8[~ maskpp8]=0

filtropp9 = datafft.copy()
filtropp9[~ maskpp9]=0

dataSint0t = fft.irfft(filtropp0t, n = len(y))
dataSint1t = fft.irfft(filtropp1t, n = len(y))
dataSint2t = fft.irfft(filtropp2t, n = len(y))
dataSint3t = fft.irfft(filtropp3t, n = len(y))
dataSint4t = fft.irfft(filtropp4t, n = len(y))
dataSint5t = fft.irfft(filtropp5t, n = len(y))

fig,ax = plt.subplots(2,3, figsize=(12,12) )
ax[0][0].set_title( 'picchi principali solo termine centrale')
ax[0][1].set_title( 'picchi principali 1 termine ai lati')
ax[0][2].set_title( 'picchi principali 2 termini ai lati')
ax[1][0].set_title( 'picchi principali 3 termini ai lati')
ax[1][1].set_title( 'picchi principali 4 termini ai lati')
ax[1][2].set_title( 'picchi principali 5 termine ai lati')

ax[0][0].plot(x, y, color = 'coral', alpha = 0.8, label = 'segnale originale')
ax[0][1].plot(x, y, color = 'coral', alpha = 0.8, label = 'segnale originale')
ax[0][2].plot(x, y, color = 'coral', alpha = 0.8, label = 'segnale originale')
ax[1][0].plot(x, y, color = 'coral', alpha = 0.8, label = 'segnale originale')
ax[1][1].plot(x, y, color = 'coral', alpha = 0.8, label = 'segnale originale')
ax[1][2].plot(x, y, color = 'coral', alpha = 0.8, label = 'segnale originale')

ax[0][0].plot(x, dataSint0t, alpha = 0.8, label = 'segnale filtrato')
ax[0][1].plot(x, dataSint1t, alpha = 0.8, label = 'segnale filtrato')
ax[0][2].plot(x, dataSint2t, alpha = 0.8, label = 'segnale filtrato')
ax[1][0].plot(x, dataSint3t, alpha = 0.8, label = 'segnale filtrato')
ax[1][1].plot(x, dataSint4t, alpha = 0.8, label = 'segnale filtrato')
ax[1][2].plot(x, dataSint5t, alpha = 0.8, label = 'segnale filtrato')

ax[0][0].legend()
ax[0][1].legend()
ax[0][2].legend()
ax[1][1].legend()
ax[1][0].legend()
ax[1][2].legend()

'''
ax[0][0].set_xlim(1, 1.10)
ax[0][1].set_xlim(1, 1.10)
ax[0][2].set_xlim(1, 1.10)
ax[1][0].set_xlim(1, 1.10)
ax[1][1].set_xlim(1, 1.10)
ax[1][2].set_xlim(1, 1.10)
'''

ax[0][0].set_xlabel('Tempo(s)')
ax[0][0].set_ylabel('Ampiezza (u.a)')
ax[0][1].set_xlabel('Tempo(s)')
ax[0][1].set_ylabel('Ampiezza (u.a)')
ax[0][2].set_xlabel('Tempo(s)')
ax[0][2].set_ylabel('Ampiezza (u.a)')
ax[1][1].set_xlabel('Tempo(s)')
ax[1][1].set_ylabel('Ampiezza (u.a)')
ax[1][0].set_xlabel('Tempo(s)')
ax[1][0].set_ylabel('Ampiezza (u.a)')
ax[1][2].set_xlabel('Tempo(s)')
ax[1][2].set_ylabel('Ampiezza (u.a)')

plt.show()

#grafico picchi selezionati


fig2,ax2 = plt.subplots(2,2, figsize=(12,12) )

ax2[0][0].set_title('Picco principale')
ax2[0][1].set_title('Primi due picchi principali')
ax2[1][0].set_title('Picchi principali solo termine centrale')
ax2[1][1].set_title('Picchi principali con due termine ai lati')

ax2[0][0].plot(fftfreq, p,'-', markersize = 1, color='seagreen', label = 'segnale originale')
ax2[1][0].plot(fftfreq, p,'-', markersize = 1, color='seagreen', label = 'segnale originale')
ax2[0][1].plot(fftfreq, p,'-', markersize = 1, color='seagreen', label = 'segnale originale')
ax2[1][1].plot(fftfreq, p,'-', markersize = 1, color='seagreen', label = 'segnale originale')

ax2[0][0].plot(fftfreq[maskpp], p[maskpp], 'o', color='deepskyblue', alpha = 0.8)
ax2[0][1].plot(fftfreq[maskpp2], p[maskpp2], 'o', color='deepskyblue', alpha = 0.8)
ax2[1][0].plot(fftfreq[maskpp3], p[maskpp3], 'o', color='deepskyblue', alpha = 0.8)
ax2[1][1].plot(fftfreq[maskpp4], p[maskpp4], 'o', color='deepskyblue', alpha = 0.8)


ax2[0][0].legend()
ax2[0][1].legend()
ax2[1][1].legend()
ax2[1][0].legend()


ax2[0][0].set_xlabel('Frequenza (Hz)')
ax2[0][0].set_ylabel('Ampiezza (u.a)')
ax2[0][1].set_xlabel('Frequenza (Hz)')
ax2[0][1].set_ylabel('Ampiezza (u.a)')
ax2[1][1].set_xlabel('Frequenza (Hz)')
ax2[1][1].set_ylabel('Ampiezza (u.a)')
ax2[1][0].set_xlabel('Frequenza (Hz)')
ax2[1][0].set_ylabel('Ampiezza (u.a)')

plt.show()



#risintetizziamo i dati filtrati
dataSint1 = fft.irfft(filtropp, n = len(y))
dataSint2 = fft.irfft(filtropp2, n = len(y))
dataSint3 = fft.irfft(filtropp3, n = len(y))
dataSint4 = fft.irfft(filtropp4, n = len(y))
dataSint5 = fft.irfft(filtropp5, n = len(y))
dataSint6 = fft.irfft(filtropp6, n = len(y))
dataSint7 = fft.irfft(filtropp7, n = len(y))
dataSint8 = fft.irfft(filtropp8, n = len(y))
dataSint9 = fft.irfft(filtropp9, n = len(y))

#produco file audio
                       
sf.write('notaSempliceDataSint1.wav', dataSint1, samplerate)
sf.write('notaSempliceDataSint2.wav', dataSint2, samplerate)
sf.write('notaSempliceDataSint3.wav', dataSint3, samplerate)
sf.write('notaSempliceDataSint4.wav', dataSint4, samplerate)
sf.write('notaSempliceDataSint5.wav', dataSint5, samplerate)
sf.write('notaSempliceDataSint6.wav', dataSint6, samplerate)
sf.write('notaSempliceDataSint7.wav', dataSint7, samplerate)
sf.write('notaSempliceDataSint8.wav', dataSint8, samplerate)
sf.write('notaSempliceDataSint9.wav', dataSint9, samplerate)

#grafico waveform

#grafico waveform

fig,ax = plt.subplots(2,2, figsize=(12,12) )
ax[0][0].set_title('picco principale')
ax[0][1].set_title( 'primi due picchi principali')
ax[1][0].set_title('picchi principali solo termine centrale')
ax[1][1].set_title('picchi principali con un termine ai lati')

ax[0][0].plot(x, y, color = 'coral', alpha = 0.8, label = 'segnale originale')
ax[0][1].plot(x, y, color = 'coral', alpha = 0.8, label = 'segnale originale')
ax[1][0].plot(x, y, color = 'coral', alpha = 0.8, label = 'segnale originale')
ax[1][1].plot(x, y, color = 'coral', alpha = 0.8, label = 'segnale originale')

ax[0][0].plot(x, dataSint2, alpha = 0.8, label = 'segnale filtrato')
ax[0][1].plot(x, dataSint5, alpha = 0.8, label = 'segnale filtrato')
ax[1][0].plot(x, dataSint3, alpha = 0.8, label = 'segnale filtrato')
ax[1][1].plot(x, dataSint4, alpha = 0.8, label = 'segnale filtrato')

ax[0][0].legend()
ax[0][1].legend()
ax[1][1].legend()
ax[1][0].legend()


ax[0][0].set_xlabel('Tempo(s)')
ax[0][0].set_ylabel('Ampiezza (u.a)')
ax[0][1].set_xlabel('Tempo(s)')
ax[0][1].set_ylabel('Ampiezza (u.a)')
ax[1][1].set_xlabel('Tempo(s)')
ax[1][1].set_ylabel('Ampiezza (u.a)')
ax[1][0].set_xlabel('Tempo(s)')
ax[1][0].set_ylabel('Ampiezza (u.a)')


plt.show()


fig,ax = plt.subplots(2,3, figsize=(12,12) )
ax[0][0].set_title( 'picco principale')
ax[0][1].set_title( 'primi due picchi principali')
ax[0][2].set_title( 'primi tre picchi principali')
ax[1][0].set_title( 'primi quattro picchi principali')
ax[1][1].set_title( 'primi cinque picchi principali')
ax[1][2].set_title( 'primi sei picchi principali')

ax[0][0].plot(x, y, color = 'coral', alpha = 0.8, label = 'segnale originale')
ax[0][1].plot(x, y, color = 'coral', alpha = 0.8, label = 'segnale originale')
ax[0][2].plot(x, y, color = 'coral', alpha = 0.8, label = 'segnale originale')
ax[1][0].plot(x, y, color = 'coral', alpha = 0.8, label = 'segnale originale')
ax[1][1].plot(x, y, color = 'coral', alpha = 0.8, label = 'segnale originale')
ax[1][2].plot(x, y, color = 'coral', alpha = 0.8, label = 'segnale originale')

ax[0][0].plot(x, dataSint2, alpha = 0.8, label = 'segnale filtrato')
ax[0][1].plot(x, dataSint5, alpha = 0.8, label = 'segnale filtrato')
ax[0][2].plot(x, dataSint6, alpha = 0.8, label = 'segnale filtrato')
ax[1][0].plot(x, dataSint7, alpha = 0.8, label = 'segnale filtrato')
ax[1][1].plot(x, dataSint8, alpha = 0.8, label = 'segnale filtrato')
ax[1][2].plot(x, dataSint9, alpha = 0.8, label = 'segnale filtrato')

ax[0][0].legend()
ax[0][1].legend()
ax[0][2].legend()
ax[1][1].legend()
ax[1][0].legend()
ax[1][2].legend()

ax[0][0].set_xlim(1, 1.10)
ax[0][1].set_xlim(1, 1.10)
ax[0][2].set_xlim(1, 1.10)
ax[1][0].set_xlim(1, 1.10)
ax[1][1].set_xlim(1, 1.10)
ax[1][2].set_xlim(1, 1.10)


ax[0][0].set_xlabel('Tempo(s)')
ax[0][0].set_ylabel('Ampiezza (u.a)')
ax[0][1].set_xlabel('Tempo(s)')
ax[0][1].set_ylabel('Ampiezza (u.a)')
ax[0][2].set_xlabel('Tempo(s)')
ax[0][2].set_ylabel('Ampiezza (u.a)')
ax[1][1].set_xlabel('Tempo(s)')
ax[1][1].set_ylabel('Ampiezza (u.a)')
ax[1][0].set_xlabel('Tempo(s)')
ax[1][0].set_ylabel('Ampiezza (u.a)')
ax[1][2].set_xlabel('Tempo(s)')
ax[1][2].set_ylabel('Ampiezza (u.a)')

plt.show()
