import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

der_100 = pd.read_csv('der_100.csv')
print(der_100)

f  = np.array(der_100['FREQUENZE'])
v_in =np.array(der_100['V_IN'])
v_out = np.array(der_100['V_OUT'])
print('v_in = ', v_in)

guadagno = v_out/v_in
plt.plot(f, guadagno)
plt.xscale('log')
plt.show()

