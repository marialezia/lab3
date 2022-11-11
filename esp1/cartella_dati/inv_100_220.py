import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

inv_100_220 = pd.read_csv('inv_100_220.csv')
print(inv_100_220)

f  = np.array(inv_100_220['FREQUENZA'])
v_in =np.array(inv_100_220['V_IN'])
v_out = np.array(inv_100_220['V_OUT'])
print('v_in = ', v_in)

guadagno = v_out/v_in
plt.plot(f, guadagno)
plt.xscale('log')
plt.show()

