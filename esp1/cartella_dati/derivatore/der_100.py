import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def g(F, R, C):
    return 2*np.pi*R*C*F

der_100 = pd.read_csv('dati_der_100.csv')
print(der_100)

r = 98
c = 10**(-6)
r_err = 0.1 #prova
c_err = 10**(-8) #prova

f_taglio = 1/(np.pi*2*r*c)
f_taglio_sperimentale = 1645
print('la frequenza di taglio teorica è ', f_taglio)
print('la frequenza di taglio sperimentale è ', f_taglio_sperimentale)

f  = np.array(der_100['FREQUENZE'])
v_in =np.array(der_100['V_IN'])
v_out = np.array(der_100['V_OUT'])

guadagno_teor = g(f, r, c)
guadagno = v_out/v_in
plt.plot(f, guadagno, '-o')
plt.plot(f, guadagno_teor)

plt.show()
