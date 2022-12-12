import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#definisco funzioni per calcolare g e errore
def gravita(f,l):
    return f**2*l*np.pi**2

def gravita_err(l,f,l_err,f_err):
    return f*np.pi**2*np.sqrt(4*l**2*f_err**2+f**2*l_err**2)

def gravita2(T,l):
    return 4*np.pi**2*l/T**2
'''
#dati da csv
dati = pd.read_csv('dati2.csv')
f = dati['frequenza'].values
l = dati['lunghezza'].values
T2 = dati['periodo'].values
T = T2*2

f_err = np.full(len(f), 0.03) 
l_err = np.full(len(l), 0.001) 

#calcolo g e propago errore
g = gravita(f,l)
g2 = gravita2(T,l)
g_err = gravita_err(l,f,l_err,f_err)

print('g = ', g2)
#print(g_err)

dati2 = pd.read_csv('oscilloscopio.csv')
volt = dati2['Volt'].values
plt.plot(volt)
plt.show()

dati3 = pd.read_csv('oscilloscopio2.csv')
volt = dati3['Volt'].values
plt.plot(volt, '-o')
plt.grid()
plt.show()


'''

