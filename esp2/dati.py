import numpy as np
import pandas as pd

resistenze = np.array([10, 27, 33, 39, 1200, 68000, 220])
resistenzeErr = 0.05*resistenze

Vref1 = np.array([310,310,310,258])
Vref2 = np.array([313,318,319,267])
Vref3 = np.array([316,326,328,277])
Vref4 = np.array([319,333,337,287])

Vref1Err = 0.005*Vref1+0.2
Vref2Err = 0.005*Vref1+0.2
Vref3Err = 0.005*Vref1+0.2
Vref4Err = 0.005*Vref1+0.2

rTab = pd.DataFrame()
rTab['R'] = resistenze
rTab['Rerr'] = resistenzeErr

tabella = pd.DataFrame()
tabella['Vref1'] = Vref1
tabella['Vref1 Err'] = Vref1Err
tabella['Vref2'] = Vref2
tabella['Vref2 Err'] = Vref2Err
tabella['Vref3'] = Vref2
tabella['Vref3 Err'] = Vref3Err
tabella['Vref4'] = Vref4
tabella['Vref4 Err'] = Vref4Err
print(tabella)
print(rTab)
tabella.to_csv('dati.csv')
rTab.to_csv('resistenze.csv')
