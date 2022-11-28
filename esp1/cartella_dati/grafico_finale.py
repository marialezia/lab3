import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize


#INVERTENTE 217_220: dati da file csv, calcolo guadagno e propagazione errori

inv_217_220 = pd.read_csv('~/lab3/esp1/cartella_dati/invertente/dati_217_220.csv')

f22  = np.array(inv_217_220['FREQUENZA'])
v22_in =np.array(inv_217_220['V_IN'])
v22_out = np.array(inv_217_220['V_OUT'])

f22_err = np.array([1,100,100,100,100,100,100,100]) #prova
v22_in_err = np.full(len(v22_in), 0.01) #prova
v22_out_err = np.full(len(v22_out), 0.01) #prova

guadagno22 = v22_out/v22_in
guadagno22_err = np.sqrt(v22_out_err**2+v22_in_err**2*v22_out**2/(v22_in**2))/v22_in

#INVERTENTE 220_100: dati da file csv, calcolo guadagno e propagazione errori

inv_220_100 = pd.read_csv('~/lab3/esp1/cartella_dati/invertente/dati_220_100.csv')

f21  = np.array(inv_220_100['FREQUENZA'])
v21_in =np.array(inv_220_100['V_IN'])
v21_out = np.array(inv_220_100['V_OUT'])


f21_err = np.array([1,1,100,100,100,100,100,100,100]) #prova
v21_in_err = np.full(len(v21_in), 0.01) #prova
v21_out_err = np.full(len(v21_out), 0.01) #prova

guadagno21 = v21_out/v21_in
guadagno21_err = np.sqrt(v21_out_err**2+v21_in_err**2*v21_out**2/(v21_in**2))/v21_in

#INVERTENTE 100_220: dati da file csv, calcolo guadagno e propagazione errori

inv_100_220 = pd.read_csv('~/lab3/esp1/cartella_dati/invertente/dati_100_220.csv')

f12  = np.array(inv_100_220['FREQUENZA'])
v12_in =np.array(inv_100_220['V_IN'])
v12_out = np.array(inv_100_220['V_OUT'])

f12_err = np.array([1,1,100,100,100,100,100,100,100]) #prova
v12_in_err = np.full(len(v12_in), 0.01) #prova
v12_out_err = np.full(len(v12_out), 0.01) #prova

guadagno12 = v12_out/v12_in
guadagno12_err = np.sqrt(v12_out_err**2+v12_in_err**2*v12_out**2/(v12_in**2))/v12_in

#calcolo guadagno teorico

A22 = np.full(len(v22_in),217/215)
A21 = np.full(len(v21_in),217/98)
A12 = np.full(len(v12_in), 98/217)


#grafici separati invertente

'''
fig, ax = plt.subplots(1,3, figsize = (36,6))

ax[0].errorbar(f22, guadagno22, xerr = f22_err, yerr = guadagno22_err, color = 'pink', label = 'invertente 217_215')
ax[1].errorbar(f21, guadagno21, xerr = f21_err, yerr = guadagno21_err, color = 'lightseagreen', label = 'invertente 217_98')
ax[2].errorbar(f12, guadagno12, xerr = f12_err, yerr = guadagno12_err, color = 'rebeccapurple', label = 'invertente 98_217')

ax[0].set_xlabel('Frequenza (Hz)')
ax[0].set_ylabel('Guadagno ')
ax[0].set_xscale('log')
ax[0].set_yscale('log')

ax[1].set_xlabel('Frequenza (Hz)')
ax[1].set_ylabel('Guadagno ')
ax[1].set_xscale('log')
ax[1].set_yscale('log')

ax[2].set_xlabel('Frequenza (Hz)')
ax[2].set_ylabel('Guadagno ')
ax[2].set_xscale('log')
ax[2].set_yscale('log')

plt.legend()
plt.show()
'''

#grafico tutti insieme invertente
plt.errorbar(f22, guadagno22, xerr = f22_err, yerr = guadagno22_err, fmt = '-o', markersize = 3, color = 'pink', label = 'invertente $R_1= 217 \ \Omega$ e $R_2 =  215 \ \Omega$')
plt.errorbar(f21, guadagno21, xerr = f21_err, yerr = guadagno21_err,fmt ='-o',  markersize = 3, color = 'lightseagreen', label =  'invertente $R_1= 217 \ \Omega$ e $R_2 =  98 \ \Omega$')
plt.errorbar(f12, guadagno12, xerr = f12_err, yerr = guadagno12_err, fmt ='-o',  markersize = 3, color = 'rebeccapurple', label =  'invertente $R_1= 98 \ \Omega$ e $R_2 =  217 \ \Omega$')
plt.xscale('log')
plt.plot(f22, A22, color = 'palevioletred', alpha= 0.5)
plt.plot(f12, A12, color = 'teal', alpha = 0.5)
plt.plot(f21, A21, color = 'indigo', alpha = 0.5)

plt.yscale('log')
plt.legend()
plt.grid()

plt.show()

#fit rette guadagno

def retta(x, m, q):
    return m*np.log10(x)+np.log10(q)

pstart = np.array([100, 1])
par12, par_cov12 = optimize.curve_fit(retta, f12[6:f12.size], guadagno12[6:f12.size], p0=[pstart])
par22, par_cov22 = optimize.curve_fit(retta, f22[3:f22.size], guadagno22[3:f22.size], p0=[pstart])
par21, par_cov21 = optimize.curve_fit(retta, f21[3:f21.size], guadagno21[3:f21.size], p0=[pstart])

y12=retta(f12[6:f12.size], par12[0], par12[1])
y22=retta(f22[3:f22.size], par22[0], par22[1])
y21=retta(f21[3:f21.size], par21[0], par21[1])

'''
plt.errorbar(f22[3:f22.size], guadagno22[3:f22.size], xerr = f22_err[3:f22.size], yerr = guadagno22_err[3:f22.size], fmt = '-o', color = 'pink', label = 'invertente 217_220')
plt.errorbar(f21[3:f21.size], guadagno21[3:f21.size], xerr = f21_err[3:f21.size], yerr = guadagno21_err[3:f21.size],fmt = '-o',  color = 'lightseagreen', label = 'invertente 220_100')
plt.errorbar(f12[6:f12.size], guadagno12[6:f12.size], xerr = f12_err[6:f12.size], yerr = guadagno12_err[6:f12.size], fmt = '-o', color = 'rebeccapurple', label = 'invertente 100_220')
plt.xscale('log')
plt.yscale('log')
plt.show()
'''

plt.plot(f22[3:f22.size], y22, color='magenta', label='fit 217_220')
plt.plot(f21[3:f21.size], y21, color='aqua', label='fit 220_100')
plt.plot(f12[6:f12.size], y12, color='violet', label='fit 100_220')
#plt.xscale('log')
#plt.yscale('log')
plt.legend()

plt.show()

print('parametri 100_200: ', par12)
print('parametri 200_200: ', par22)
print('parametri 200_100: ', par21)
