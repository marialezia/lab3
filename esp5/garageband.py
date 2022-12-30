import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants, fft

#apro il file .wav
data, samplerate = sf.read('diapason.wav')

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
plt.title('Waveform diapason')
plt.plot(x, y, color = 'seagreen')
plt.xlabel('Tempo[s]')
plt.ylabel('Ampiezza (u.a)')
plt.show()
'''
#creo un nuovo file .wav uguale al primo
#sf.write('diapason_recreated.wav', data, samplerate)

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
#grafico potenza con massimi
p=np.absolute(datafft)**2

max1 = np.argmax(p)
max2 = np.argmax(p[400:len(p)])
max3 = np.argmax(p[1800:len(p)])
'''
plt.plot(fftfreq, p, color='limegreen')
plt.plot(fftfreq[max1], p[max1], 'o', color='forestgreen')
plt.plot(fftfreq[400:len(p)][max2], p[400:len(p)][max2], 'o', color='forestgreen')
plt.plot(fftfreq[1800:len(p)][max3], p[1800:len(p)][max3], 'o', color='forestgreen')
plt.xlabel('Frequenza (hz)')
plt.ylabel('Potenza (u.a)')
plt.show()
'''
max4 = np.argmax(datafft)
max5 = np.argmax(datafft[700:1800])
max6 = np.argmax(datafft[1800:len(datafft)])
min1 = np.argmin(datafft)
min2 = np.argmin(datafft[700:len(datafft)])
min3 = np.argmin(datafft[1800:len(datafft)])
'''
#grafico parte reale con massimi e minimi
plt.plot(fftfreq, datafft.real, color='lightsalmon')
plt.plot(fftfreq[max4], datafft[max4].real, 'o', color='tomato')
plt.plot(fftfreq[700:1800][max5], datafft[700:1800][max5].real, 'o', color='tomato')
plt.plot(fftfreq[1800:len(datafft)][max6], datafft[1800:len(datafft)][max6].real, 'o', color='tomato')
plt.plot(fftfreq[min1], datafft[min1].real, 'o', color='tomato')
plt.plot(fftfreq[700:len(datafft)][min2], datafft[700:len(datafft)][min2].real, 'o', color='tomato')
plt.plot(fftfreq[1800:len(datafft)][min3], datafft[1800:len(datafft)][min3].real, 'o', color='tomato')
plt.show()
'''

#mascherare (mettere a zero) i coefficienti, tranne alcuni scelti
mask1 = p == p[max1]
mask2 = p == p[400:len(p)][max2]
mask3 = p == p[1400:len(p)][max3]

plt.plot(fftfreq[mask1], p[mask1], 'o')
plt.show()
