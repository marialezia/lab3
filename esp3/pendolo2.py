import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#definisco funzioni per calcolare g e errore

def gravita(T,l):
    return 4*np.pi**2*l/T**2

l = 0.38

#prendo dati da csv, SCALA 1S
scala_1s = pd.read_csv('scala_1s.csv')
v1s = scala_1s['Volt'].values
t1s = scala_1s['Increment'][0] #tempo di campionamento
#start1s = scala_1s['Start'][0] #tempo di start SCHERZO È UN NUMERO NEGATIVO QUINDI NON SO COSA È
#start1s = 0
#stop1s = start1s + t1s*len(v1s) #tempo di stop = tempo di start + tempo campionamento * numero campionamenti
#tempi1s = np.arange(start1s,stop1s, t1s)

#SCALA 2S PRIMA PROVA
scala_2s_1 = pd.read_csv('scala_2s_1.csv')
v2s_1 = scala_2s_1['Volt'].values
t2s_1 = scala_2s_1['Increment'][0]
#start2s_1 = scala_2s_1['Start'][0] 
#start2s_1 = 0
#stop2s_1 = start2s_1 + t2s_1*len(v2s_1) 
#tempi2s_1 = np.arange(start2s_1,stop2s_1, t2s_1)

#SCALA 2S SECONDA PROVA
scala_2s_2 = pd.read_csv('scala_2s_2.csv')
v2s_2 = scala_2s_2['Volt'].values
t2s_2 = scala_2s_2['Increment'][0] #tempo di campionamento
#start2s_2 = scala_2s_2['Start'][0] 
#start2s_2 = 0
#stop2s_2 = start2s_2 + t2s_2*len(v2s_2) 
#tempi2s_2 = np.arange(start2s_2,stop2s_2, t2s_2)

#SCALA 2S TERZA PROVA
scala_2s_3 = pd.read_csv('scala_2s_3.csv')
v2s_3 = scala_2s_3['Volt'].values
t2s_3 = scala_2s_3['Increment'][0] #tempo di campionamento
#start2s_3 = scala_2s_3['Start'][0] 
#tart2s_3 = 0
#stop2s_3 = start2s_3+ t2s_3*len(v2s_3) 
#tempi2s_3 = np.arange(start2s_3,stop2s_3, t2s_3)

#dati vecchi non so la scala
scala_xs_1 = pd.read_csv('oscilloscopio.csv')
vxs_1 = scala_xs_1['Volt'].values
txs_1 = scala_xs_1['Increment'][0] #tempo di campionamento

scala_xs_2 = pd.read_csv('oscilloscopio2.csv')
vxs_2 = scala_xs_2['Volt'].values
txs_2 = scala_xs_2['Increment'][0] #tempo di campionamento


#GRAFICI
'''
plt.plot(tempi1s, v1s, '-o', markersize = 3)
plt.title('Scala 1s')
plt.grid()
plt.xlabel('Tempo (s)')
plt.ylabel('Volt (v)')
plt.show()

plt.plot(tempi2s_1, v2s_1, '-o', markersize = 3)
plt.title('Scala 2s - prima prova')
plt.xlabel('Tempo (s)')
plt.ylabel('Volt (v)')
plt.grid()
#plt.show()

plt.plot(tempi2s_2, v2s_2,  '-o', markersize = 3)
plt.title('Scala 2s - seconda prova')
plt.xlabel('Tempo (s)')
plt.ylabel('Volt (v)')
plt.grid()
#plt.show()

#plt.plot(tempi2s_3, v2s_3, '-o', markersize = 3)
#plt.title('Scala 2s - terza prova')
#plt.grid()
#plt.show()

'''
#calcolo tempo totale dieci oscillazioni con ciclo for che guarda quando il valore del volt si abbassa sotto 6 per vedere dove ci sono i picchi 

#set 1s
prima = True
conta = 0
for i in range(len(v1s)):
    dopo = True
    if v1s[i] < 6:
        dopo =  False
    if prima != dopo:
        conta = conta+1
        if conta == 1:
            start = i
            print('start = ', start)
    if conta == 21:
        stop = i
        print('stop = ', stop)
        break
    prima = dopo

periodo1s = (stop-start)*t1s/5
g1s = gravita(periodo1s, l)


#set 2s prima prova
prima = True
conta = 0
for i in range(len(v2s_1)):
    dopo = True
    if v2s_1[i] < 6:
        dopo =  False
    if prima != dopo:
        conta = conta+1
        if conta == 1:
            start = i
            print('start = ', start)
    if conta == 21:
        stop = i
        print('stop = ', stop)
        break
    prima = dopo

periodo2s_1 = (stop-start)*t2s_1/5
g2s_1 = gravita(periodo2s_1, l)


#set 2s seconda prova

prima = True
conta = 0
for i in range(len(v2s_2)):
    dopo = True
    if v2s_2[i] < 6:
        dopo =  False
    if prima != dopo:
        conta = conta+1
        if conta == 1:
            start = i
    if conta == 21:
        stop = i
        break
    prima = dopo

periodo2s_2 = (stop-start)*t2s_2/5
g2s_2 = gravita(periodo2s_2, l)

#set 2s terza prova

prima = True
conta = 0
for i in range(len(v2s_3)):
    dopo = True
    if v2s_3[i] < 6:
        dopo =  False
    if prima != dopo:
        conta = conta+1
        if conta == 1:
            start = i
    if conta == 21:
        stop = i
        break
    prima = dopo

periodo2s_3 = (stop-start)*t2s_3/5
g2s_3 = gravita(periodo2s_3, l)


#set x prima prova

prima = True
conta = 0
for i in range(len(vxs_1)):
    dopo = True
    if vxs_1[i] < 6:
        dopo =  False
    if prima != dopo:
        conta = conta+1
        if conta == 1:
            start = i
    if conta == 13:
        stop = i
        break
    prima = dopo

periodoxs_1 = (stop-start)*txs_1/3
gxs_1 = gravita(periodoxs_1, l)


#set x seconda prova

prima = True
conta = 0
for i in range(len(vxs_2)):
    dopo = True
    if vxs_2[i] < 6:
        dopo =  False
    if prima != dopo:
        conta = conta+1
        if conta == 1:
            start = i
    if conta == 21:
        stop = i
        break
    prima = dopo

periodoxs_2 = (stop-start)*txs_2/5
gxs_2 = gravita(periodoxs_2, l)

plt.plot(vxs_1, '-o')
plt.show()

tabella = pd.DataFrame()
tabella['Scala'] = ('1s', '2s_1', '2s_2', '2s_3', 'xs_1', 'xs_2')
tabella['T'] = (periodo1s, periodo2s_1, periodo2s_2, periodo2s_3, periodoxs_1, periodoxs_2)
tabella['g'] = (g1s, g2s_1, g2s_2, g2s_3, gxs_1, gxs_2)

print(tabella)
