import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

inv_100_220 = pd.read_csv('inv_100_220.csv')
print(inv_100_220)

f  = np.array(inv_100_220['FREQUENZA'])
v_in =np.array(inv_100_220['V_IN'])
v_out = np.array(inv_100_220['V_OUT'])

f_err = np.array([1,1,100,100,100,100,100,100,100]) #prova
v_in_err = np.full(9, 0.1) #prova
v_out_err = np.full(9, 0.1) #prova

guadagno = v_out/v_in
guadagno_err = np.sqrt(v_out_err**2+v_in_err**2*v_out**2/(v_in**2))/v_in

plt.errorbar(f, guadagno, xerr = f_err, yerr = guadagno_err)
plt.xlabel('Frequenza [Hz]')
plt.ylabel('Guadagno')
#plt.xscale('log')
plt.show()

