import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('readings.dat', skiprows=1, usecols=(2, 3, 4))

morning = data[::2]
evening = data[1::2]

ax1 = plt.subplot(121)
plt.plot(morning)
plt.grid(True)
plt.title('Morning')

plt.subplot(122, sharey=ax1)
plt.plot(evening)
plt.grid(True)
plt.title('Evening')

plt.show()
