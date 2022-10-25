import numpy as np 
import soundcard as sc 
import matplotlib.pyplot as plt 

frequenza = 48000
speakers = sc.all_speakers()
print("Speaker disponibili: ", speakers, "\n")
default_speaker = sc.default_speaker()
print("Speaker selezionato: ", default_speaker, "\n")
mics = sc.all_microphones()
print("Microfoni disponibili: ", mics, "\n")
default_mic = sc.default_microphone()
print("Microfono selezionato: ", default_mic, "\n")
data = default_mic.record(samplerate=frequenza, numframes=480000)
print("Array acquisito: ")
print(data)
print("\n")
default_speaker.play(data/np.max(data), samplerate=frequenza)
print("L'array dei dati registrati è lungo ", len(data))

y = np.ones(len(data))
for i in range(len(data)):
    y[i]  = data[i][0]

t = 1/frequenza
x = np.arange(0, 10, t)

plt.title('audio')
plt.plot(x, y, color = 'pink')
plt.show()
