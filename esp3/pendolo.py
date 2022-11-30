import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def gravita(f,l):
    return f**2*l*np.pi**2
print(np.pi)
dati = pd.read_csv('dati.csv')
f = dati['frequenza']
l = dati['lunghezza']
print(f)
print(l)
#T_err = np.full(len(T), 0.01) #prova
#l_err = np.full(len(l), 0.01) #prova

g = gravita(f,l)
#g_err = 4*np.pi**2/T**2*np.sqrt(l_err**2+4*T_err**2/T**2)
print('g = ', g)


