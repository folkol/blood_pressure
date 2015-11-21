import numpy as np
import matplotlib.pyplot as plt

# fromfile = np.fromfile('readings.dat', sep=' ', count=-1)
data = np.loadtxt('readings.dat', skiprows=1, usecols=(2, 3, 4))

plt.plot(data)
plt.show()
