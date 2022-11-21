import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#dati da file csv
inv_100_220 = pd.read_csv('dati_100_220.csv')
print('DATI INVERTENTE 100_220')
print(inv_100_220)

f  = np.array(inv_100_220['FREQUENZA'])
v_in =np.array(inv_100_220['V_IN'])
v_out = np.array(inv_100_220['V_OUT'])

f_err = np.array([1,1,100,100,100,100,100,100,100]) #prova
v_in_err = np.full(len(v_in), 0.01) #prova
v_out_err = np.full(len(v_out), 0.01) #prova

#calcolo guadagno e propagazione errori
guadagno = v_out/v_in
guadagno_err = np.sqrt(v_out_err**2+v_in_err**2*v_out**2/(v_in**2))/v_in

#tabella con errori e guadagno, scrivo su csv
tabella = pd.DataFrame()
tabella['FREQUENZA (Hz)'] = f
tabella['FREQ_err (Hz)'] = f_err
tabella['V_IN (V)'] = v_in
tabella['V_IN_err (V)'] = v_in_err
tabella['V_OUT (V)'] = v_out
tabella['V_OUT_err (V)'] = v_out_err
tabella['G = V_OUT/V_IN'] = guadagno
tabella['G_err'] = guadagno_err
print(tabella)
tabella.to_csv('tabella_100_220.csv', index=False)

#grafico guadagno in funzione di frequenza
plt.errorbar(f, guadagno, xerr = f_err, yerr = guadagno_err)
plt.xlabel('Frequenza (Hz)')
plt.ylabel('Guadagno')
plt.xscale('log')
plt.show()

