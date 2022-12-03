import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize


#GUADAGNO1: dati da file csv, calcolo guadagno e propagazione errori

inv_217_220 = pd.read_csv('guadagno1.csv')

f22  = np.array(inv_217_220['FREQUENZA'])
v22_in =np.array(inv_217_220['V_IN'])
v22_out = np.array(inv_217_220['V_OUT'])

f22_err = np.array([10,10, 100,100,100,100,100,100,100,100]) 
v22_in_err = np.full(len(v22_in), 0.04) 
v22_out_err = np.full(len(v22_out), 0.04)

guadagno22 = v22_out/v22_in
guadagno22_err = np.sqrt(v22_out_err**2+v22_in_err**2*v22_out**2/(v22_in**2))/v22_in

#GUADAGNO 2: dati da file csv, calcolo guadagno e propagazione errori

inv_220_100 = pd.read_csv('guadagno2.csv')

f21  = np.array(inv_220_100['FREQUENZA'])
v21_in =np.array(inv_220_100['V_IN'])
v21_out = np.array(inv_220_100['V_OUT'])


f21_err = np.array([10,10,100,100,100,100,100,100,100,100]) 
v21_in_err = np.full(len(v21_in), 0.04) 
v21_out_err = np.full(len(v21_out), 0.04) 

guadagno21 = v21_out/v21_in
guadagno21_err = np.sqrt(v21_out_err**2+v21_in_err**2*v21_out**2/(v21_in**2))/v21_in

#GUADAGNO 0.5: dati da file csv, calcolo guadagno e propagazione errori

inv_100_220 = pd.read_csv('guadagno05.csv')

f12  = np.array(inv_100_220['FREQUENZA'])
v12_in =np.array(inv_100_220['V_IN'])
v12_out = np.array(inv_100_220['V_OUT'])

f12_err = np.array([10,10,100,100,100,100,100,100,100,100]) 
v12_in_err = np.full(len(v12_in), 0.04) 
v12_out_err = np.full(len(v12_out), 0.04)

guadagno12 = v12_out/v12_in
guadagno12_err = np.sqrt(v12_out_err**2+v12_in_err**2*v12_out**2/(v12_in**2))/v12_in



#grafico tutti insieme invertente
plt.errorbar(f22, guadagno22, yerr = guadagno22_err, fmt = '-o', markersize = 3, color = 'pink', label = 'Invertente guadagno 1')
plt.errorbar(f21, guadagno21, yerr = guadagno21_err,fmt ='-o',  markersize = 3, color = 'lightseagreen', label =  'Invertente guadagno 2')
plt.errorbar(f12, guadagno12, yerr = guadagno12_err, fmt ='-o',  markersize = 3, color = 'rebeccapurple', label =  'Invertente guadagno 0.5')
plt.xlabel('log(frequenza (Hz))')
plt.ylabel('log(guadagno)')
plt.yscale('log')
plt.xscale('log')
plt.legend()
plt.title('Invertente - Secondo set')
plt.grid()

plt.show()
'''

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


plt.errorbar(f22[3:f22.size], guadagno22[3:f22.size], xerr = f22_err[3:f22.size], yerr = guadagno22_err[3:f22.size], fmt = '-o', color = 'pink', label = 'invertente 217_220')
plt.errorbar(f21[3:f21.size], guadagno21[3:f21.size], xerr = f21_err[3:f21.size], yerr = guadagno21_err[3:f21.size],fmt = '-o',  color = 'lightseagreen', label = 'invertente 220_100')
plt.errorbar(f12[6:f12.size], guadagno12[6:f12.size], xerr = f12_err[6:f12.size], yerr = guadagno12_err[6:f12.size], fmt = '-o', color = 'rebeccapurple', label = 'invertente 100_220')
plt.xscale('log')
plt.yscale('log')
plt.show()


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
'''
