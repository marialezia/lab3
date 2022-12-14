import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#definisco funzioni per calcolare g e errore

def gravita(T,l):
    return 4*np.pi**2*l/T**2

def periodo(volt, incremento, oscillazioni):
    prima = True
    conta = 0
    for i in range(len(volt)):
        dopo = True
        if volt[i] < 6:
            dopo =  False
        if prima != dopo:
            conta = conta+1
            if conta == 1:
                start = i
        if conta == (oscillazioni*2+1):
            stop = i
            break
        prima = dopo
    periodo = (stop-start)*incremento*2/oscillazioni
    periodoErr = incremento*2/oscillazioni
    return periodo, periodoErr

def gravitaErr(T,TErr, l, lErr):
    return 4*np.pi**2/T**2*np.sqrt(lErr**2+TErr**2/T**2)

lunghezza = 0.38
lunghezzaErr = 0.0001/(12)**0.5

print(lunghezzaErr)

#prendo dati da csv, SCALA 1S
scala_1s = pd.read_csv('scala_1s.csv')
v1s = scala_1s['Volt'].values
t1s = scala_1s['Increment'][0] #tempo di campionamento
start1s = scala_1s['Start'][0] #tempo di start SCHERZO È UN NUMERO NEGATIVO QUINDI NON SO COSA È
tempi1s = np.arange(start1s,start1s+t1s*len(v1s), t1s)

#SCALA 2S PRIMA PROVA
scala_2s_1 = pd.read_csv('scala_2s_1.csv')
v2s_1 = scala_2s_1['Volt'].values
t2s_1 = scala_2s_1['Increment'][0]
start2s_1 = scala_2s_1['Start'][0] 
tempi2s_1 = np.arange(0,t2s_1*len(v2s_1), t2s_1)

#SCALA 2S SECONDA PROVA
scala_2s_2 = pd.read_csv('scala_2s_2.csv')
v2s_2 = scala_2s_2['Volt'].values
t2s_2 = scala_2s_2['Increment'][0] #tempo di campionamento
start2s_2 = scala_2s_2['Start'][0] 
tempi2s_2 = np.arange(start2s_2,start2s_2+t2s_2*len(v2s_2), t2s_2)

#SCALA 2S TERZA PROVA
scala_2s_3 = pd.read_csv('scala_2s_3.csv')
v2s_3 = scala_2s_3['Volt'].values
t2s_3 = scala_2s_3['Increment'][0] #tempo di campionamento
start2s_3 = scala_2s_3['Start'][0] 
tempi2s_3 = np.arange(start2s_3,start2s_3+t2s_3*(len(v2s_3)-1), t2s_3)


#dati vecchi non so la scala
scala_xs_1 = pd.read_csv('oscilloscopio.csv')
vxs_1 = scala_xs_1['Volt'].values
txs_1 = scala_xs_1['Increment'][0] #tempo di campionamento
startxs_1 = scala_xs_1['Start'][0]
tempixs_1 = np.arange(startxs_1,startxs_1+txs_1*len(vxs_1), txs_1)

scala_xs_2 = pd.read_csv('oscilloscopio2.csv')
vxs_2 = scala_xs_2['Volt'].values
txs_2 = scala_xs_2['Increment'][0] #tempo di campionamento
startxs_2 = scala_xs_2['Start'][0]
tempixs_2 = np.arange(startxs_2,startxs_2+txs_2*len(vxs_2), txs_2)


#GRAFICI

plt.plot(tempi1s, v1s, '-o', markersize = 3, color = 'firebrick')
plt.title('Scala 1s')
plt.grid()
plt.xlabel('Tempo (s)')
plt.ylabel('Volt (V)')
plt.show()


plt.plot(tempi2s_1, v2s_1, '-o', markersize = 3, color = 'rosybrown')
plt.title('Scala 2s - 1° prova')
plt.xlabel('Tempo (s)')
plt.ylabel('Volt (v)')
plt.grid()
plt.show()


plt.plot(tempi2s_2, v2s_2,  '-o', markersize = 3, color= 'salmon')
plt.title('Scala 2s - seconda prova')
plt.xlabel('Tempo (s)')
plt.ylabel('Volt (v)')
plt.grid()
plt.show()

plt.plot(tempi2s_3, v2s_3, '-o', markersize = 3, color = 'steelblue')
plt.title('Scala 2s - terza prova')
plt.xlabel('Tempo (s)')
plt.ylabel('Volt (v)')
plt.grid()
plt.show()

plt.plot(tempixs_1,vxs_1, '-o', markersize = 3, color = 'mediumslateblue')
plt.title('Scala xs - prima prova')
plt.xlabel('Tempo (s)')
plt.ylabel('Volt (v)')
plt.grid()
plt.show()

plt.plot(tempixs_2,vxs_2, '-o', markersize = 3, color= 'rebeccapurple')
plt.title('Scala xs - seconda prova')
plt.xlabel('Tempo (s)')
plt.ylabel('Volt (v)')
plt.grid()
plt.show()


