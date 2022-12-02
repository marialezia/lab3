import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#dati da file csv
inv_100_220 = pd.read_csv('guadagno1.csv')
print('DATI INVERTENTE 100_220')
print(inv_100_220)

f1  = np.array(inv_100_220['FREQUENZA'])
v_in1 =np.array(inv_100_220['V_IN'])
v_out1 = np.array(inv_100_220['V_OUT'])

f_err1 = np.array([1,1,100,100,100,100,100,100,100,100]) #prova
v_in_err1 = np.full(len(v_in1), 0.01) #prova
v_out_err1 = np.full(len(v_out1), 0.01) #prova

#calcolo guadagno e propagazione errori
guadagno1 = v_out1/v_in1
guadagno_err1 = np.sqrt(v_out_err1**2+v_in_err1**2*v_out1**2/(v_in1**2))/v_in1


inv_220_100 = pd.read_csv('guadagno2.csv')
print('DATI INVERTENTE 220_100')
print(inv_220_100)

f2  = np.array(inv_220_100['FREQUENZA'])
v_in2 =np.array(inv_220_100['V_IN'])
v_out2 = np.array(inv_220_100['V_OUT'])

f_err2 = np.array([1,1,100,100,100,100,100,100,100,100]) #prova
v_in_err2 = np.full(len(v_in2), 0.01) #prova
v_out_err2 = np.full(len(v_out2), 0.01) #prova

#calcolo guadagno e propagazione errori
guadagno2 = v_out2/v_in2
guadagno_err2 = np.sqrt(v_out_err2**2+v_in_err2**2*v_out2**2/(v_in2**2))/v_in2


#dati da csv
inv_217_220 = pd.read_csv('guadagno05.csv')
print('DATI INVERTENTE 217_220')
print(inv_217_220)

f05  = np.array(inv_217_220['FREQUENZA'])
v_in05 =np.array(inv_217_220['V_IN'])
v_out05 = np.array(inv_217_220['V_OUT'])

f_err05 = np.array([1,100,100,100,100,100,100,100,100,100]) #prova
v_in_err05 = np.full(len(v_in05), 0.01) #prova
v_out_err05 = np.full(len(v_out05), 0.01) #prova

#calcolo guadagno e propagazione errori
guadagno05 = v_out05/v_in05
guadagno_err05 = np.sqrt(v_out_err05**2+v_in_err05**2*v_out05**2/(v_in05**2))/v_in05



#grafico guadagno in funzione di frequenza
plt.errorbar(f1, guadagno1, xerr = f_err1, yerr = guadagno_err1, fmt = '-o')
plt.errorbar(f2, guadagno2, xerr = f_err2, yerr = guadagno_err2, fmt = '-o')
plt.errorbar(f05, guadagno05, xerr = f_err05, yerr = guadagno_err05, fmt = '-o')

plt.xlabel('Frequenza (Hz)')
plt.ylabel('Guadagno')
plt.xscale('log')
plt.yscale('log')
plt.show()
