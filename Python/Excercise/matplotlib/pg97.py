import matplotlib.pyplot as plt 
import numpy as np 
x = np.arange(0.0, 2, 0.01) 
#x = np.arange(1, 5, 1) 
y1 = np.sin(2* np.pi *x) 
y2 = 1.2 * np.sin(4 * np.pi * x) 
fig, ax = plt.subplots (1, sharex=True) 
ax.plot(x, y1, x, y2, color='black') 
ax.fill_between (x, y1, y2, where=y2 >= y1, facecolor='blue') 
ax.fill_between (x, y1, y2, where=y2 <= y1, facecolor='red') 
ax.set_title('fill between where') 
plt.show()