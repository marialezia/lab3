import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize

def g(F, R, C):
    return 2*np.pi*R*C*F

#dati da file csv
der_100 = pd.read_csv('dati_der_100.csv')
print(der_100)

f  = np.array(der_100['FREQUENZE'])
v_in =np.array(der_100['V_IN'])
v_out = np.array(der_100['V_OUT'])

f_err = np.array([1,10,10,10,10,10,10,10,100,100,100,100]) #risoluzione generatore segnale
v_in_err = np.full(len(v_in), 0.04) 
v_out_err = np.full(len(v_out), 0.04)

#calcolo frequenza di taglio e propagazione errori
r = 98
c = 10**(-6)
r_err = r*0.008+0.2 #+- 0.8% + 2 digit
c_err = 10**(-6)*0.10 #10% POI CONTROLLIAMO IN LABORATORIO

f_taglio = 1/(np.pi*2*r*c)
f_taglio_err = (r_err**2/r**2+c_err**2/c**2)**0.5/(np.pi*2*r*c)

f_taglio_sperimentale = 1645
f_taglio_sperimentale_err = 10 #risoluzione generatore segnali


print('la frequenza di taglio teorica è ', f_taglio)
print('la frequenza di taglio sperimentale è ', f_taglio_sperimentale)

#calcolo guadagno e propagazione errori
guadagno_teor = g(f, r, c)
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
tabella.to_csv('tabella_der.csv', index=False)

#grafico guadagno in funzione di frequenza
plt.errorbar(f, guadagno, xerr = f_err, yerr = guadagno_err)
plt.xlabel('Frequenza (Hz)')
plt.ylabel('Guadagno')
plt.xscale('log')
plt.show()


#fit dati range dati 0-6

pstart = np.array([100, 0.000001])
par, par_cov = optimize.curve_fit(g, f[:8], guadagno[:8], p0=[pstart])
par_err = np.sqrt(par_cov.diagonal())

y=g(f[:8], par[0], par[1])

plt.plot(f, guadagno_teor,color = 'lightgreen' , linewidth= 3, label='Retta teorica', alpha = 0.8)
plt.plot(f[:8], y, label='Fit', color = 'teal')
#plt.plot(f[:8], guadagno[:8], '-o',markersize = 3, color = 'seagreen', label='Retta dati', alpha = 0.8)
plt.plot(f, guadagno, '-o',markersize = 3, color = 'indigo', linewidth= 1.5,label='Retta dati', alpha = 0.8)

plt.legend()
plt.grid()
plt.xlabel('log(frequenza (Hz))')
plt.ylabel('log(guadagno)')
plt.xscale('log')
plt.yscale('log')
plt.title('Derivatore')
plt.show()

print('parametri: ', par)
freq_fit = 1/(2*np.pi*par[0]*par[1])
freq_fit_err = (par_err[0]**2/par[0]**2+par_err[1]**2/par[1]**2)**0.5/(np.pi*2*par[0]*par[1])
print('frequenza di taglio fit: ', freq_fit)

#tabella con frequenza di taglio teorica, sperimentale, fit, su csv
tabella2 = pd.DataFrame(index = ['Teorica', 'Sperimentale', 'Fit'])
tabella2['Frequenza di taglio (Hz)'] = [f_taglio, f_taglio_sperimentale, freq_fit]
tabella2['Errore (Hz)'] = [f_taglio_err, f_taglio_sperimentale_err, freq_fit_err]

print(tabella2)
tabella2.to_csv('tabella_f_taglio.csv', index=True)
