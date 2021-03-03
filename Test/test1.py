import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp1d
import numpy as np

# df['year'] = ['2005, 2005, 2005, 2015, 2015, 2015, 2030, 2030, 2030']
# df['name'] = ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']
# df['weight'] = [80, 65, 88, 65, 60, 70, 60, 55, 65]

df1 = pd.DataFrame()
df1['Weight_A'] = [80, 65,  60 ,59]
df1['Weight_B'] = [65, 60,  55 ,54]
df1['Weight_C'] = [88, 70,  65 ,64]
df1.index = [2005,2015,2030,2031]


ax = df1.plot.line()
ax.set_title('Before interpolation')
ax.set_xlabel("year")
ax.set_ylabel("weight")

f1 = interp1d(df1.index, df1['Weight_A'],kind='cubic')
f2 = interp1d(df1.index, df1['Weight_B'],kind='cubic')
f3 = interp1d(df1.index, df1['Weight_C'],kind='cubic')

df2 = pd.DataFrame()
new_index = np.arange(2005,2031)
df2['Weight_A'] = f1(new_index)
df2['Weight_B'] = f2(new_index)
df2['Weight_C'] = f3(new_index)
df2.index = new_index

ax2 = df2.plot.line()
ax2.set_title('After interpolation')
ax2.set_xlabel("year")
ax2.set_ylabel("weight")


plt.show()