import matplotlib.pyplot as plt 
import numpy as np

fig = plt.figure() 
a = np.linspace(-np.pi, np.pi, 256)
b = np.sin(a)
plt.plot(a, b) 
fig.savefig('temp.png', dpi=fig.dpi)