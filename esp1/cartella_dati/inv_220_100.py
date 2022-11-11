import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

inv_220_100 = pd.read_csv('inv_220_100.csv')
print(inv_220_100)

f  = np.array(inv_220_100['FREQUENZA'])
v_in =np.array(inv_220_100['V_IN'])
v_out = np.array(inv_220_100['V_OUT'])
print('v_in = ', v_in)

guadagno = v_out/v_in
plt.plot(f, guadagno)
plt.show()
