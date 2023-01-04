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

lunghezza = 0.381
lunghezzaErr = 0.001/(12)**0.5
lunghezzaErrRel = lunghezzaErr/lunghezza


#SCALA 2S PRIMA PROVA
scala_2s_1 = pd.read_csv('scala_2s_1.csv')
v2s_1 = scala_2s_1['Volt'].values
t2s_1 = scala_2s_1['Increment'][0]
start2s_1 = scala_2s_1['Start'][0] 
tempi2s_1 = np.arange(start2s_1,start2s_1+t2s_1*len(v2s_1), t2s_1)
print(len(v2s_1))

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

#SCALA 2S QUARTA PROVA

scala_2s_4 = pd.read_csv('oscilloscopio2.csv')
v2s_4 = scala_2s_2['Volt'].values
t2s_4 = scala_2s_2['Increment'][0] #tempo di campionamento
start2s_4 = scala_2s_2['Start'][0]
tempi2s_4 = np.arange(start2s_2,start2s_2+t2s_2*len(v2s_2), t2s_2)

# SCALA 1S
scala_1s = pd.read_csv('scala_1s.csv')
v1s = scala_1s['Volt'].values
t1s = scala_1s['Increment'][0] #tempo di campionamento
start1s = scala_1s['Start'][0] #tempo di start SCHERZO È UN NUMERO NEGATIVO QUINDI NON SO COSA È
tempi1s = np.arange(start1s,start1s+t1s*len(v1s), t1s)

#SCALA 0.5s
scala_xs_1 = pd.read_csv('oscilloscopio.csv')
vxs_1 = scala_xs_1['Volt'].values
txs_1 = scala_xs_1['Increment'][0] #tempo di campionamento
startxs_1 = scala_xs_1['Start'][0]
tempixs_1 = np.arange(startxs_1,startxs_1+txs_1*len(vxs_1), txs_1)


#calcolo tempo totale dieci oscillazioni con ciclo for che guarda quando il valore del volt si abbassa sotto 6 per vedere dove ci sono i picchi 

#set 1s
periodo1s, periodoErr1s =  periodo(v1s, t1s, 18)

#set 2s prima prova
periodo2sp1, periodoErr2sp1 = periodo(v2s_1, t2s_1, 18)

#set 2s seconda prova
periodo2sp2, periodoErr2sp2= periodo(v2s_2, t2s_2, 18)

#set 2s terza prova
periodo2sp3,  periodoErr2sp3 = periodo(v2s_3, t2s_3, 18)

#set 2s quarta prova (2s)
periodo2sp4,  periodoErr2sp4 = periodo(v2s_4, t2s_4, 18)

#set x prima prova (0.5s)
periodoxs, periodoErrxs = periodo(vxs_1, txs_1, 6 )


periodoArr = np.array([periodo1s, periodo2sp1, periodo2sp2, periodo2sp3, periodo2sp4, periodoxs])
periodoArrErr = np.array([periodoErr1s, periodoErr2sp1, periodoErr2sp2, periodoErr2sp3, periodoErr2sp4, periodoErrxs])
periodoErr = np.std(periodoArr, ddof = 1)
periodo = np.mean(periodoArr)
print(periodoArr, periodoArrErr)
print(periodo, periodoErr)
periodoErrRel = periodoErr/periodo

g = gravita(periodo, lunghezza)
gErr = gravitaErr(periodo, periodoErr, lunghezza, lunghezzaErr)
gErrRel = gErr/g


tabella = pd.DataFrame()
tabella['Scala'] = ('0.5 s','1s', '2s 1° prova', '2s 2° prova', '2s 3° prova', '2s 4°prova')
tabella['T'] = (periodoxs, periodo1s, periodo2sp1, periodo2sp2, periodo2sp3, periodo2sp4)
tabella['T err'] = (periodoErrxs, periodoErr1s, periodoErr2sp1, periodoErr2sp2, periodoErr2sp3, periodoErr2sp4)
tabella['Incremento'] = (txs_1, t1s, t2s_1, t2s_2, t2s_3, t2s_4)

print(tabella)
tabella.to_csv('periodi.csv', index=False)

tabella2 = pd.DataFrame(index=['Periodo (s)', 'Lunghezza (m)', 'Gravità (m/s^2)'])
tabella2['Valore'] = (periodo, lunghezza, g)
tabella2['Errore assoluto'] = (periodoErr, lunghezzaErr, gErr)
tabella2['Errore relativo'] = (periodoErrRel, lunghezzaErrRel,gErrRel)

print(tabella2)
tabella2.to_csv('risultati.csv', index=True)
