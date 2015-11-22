import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('readings.dat', skiprows=1, usecols=(2, 3))


morning = data[::2]
title = 'Morning'
ax1 = plt.subplot(121)
plt.plot(morning)
plt.grid(True)
plt.title(title)
sys = morning[:, 0]
dia = morning[:, 1]
plt.legend([
    'SYS:\t${(min=%5.d, max=%d, mean=%d)}$' % (sys.min(), sys.max(), sys.mean()),
    'DIA:\t${(min=%d, max=%d, mean=%d)}$' % (dia.min(), dia.max(), dia.mean())
], loc=2, fancybox=True)
plt.axhline(sys.mean(), linestyle='--', linewidth=0.5)
plt.axhline(dia.mean(), linestyle='--', linewidth=0.5)
plt.xticks([])

evening = data[1::2]
title = 'Evening'
plt.subplot(122, sharey=ax1)
plt.plot(evening)
plt.grid(True)
plt.title(title)
sys = evening[:, 0]
dia = evening[:, 1]
plt.legend([
    'SYS:\t${(min=%5.d, max=%d, mean=%d)}$' % (sys.min(), sys.max(), sys.mean()),
    'DIA:\t${(min=%d, max=%d, mean=%d)}$' % (dia.min(), dia.max(), dia.mean())
], loc=2, fancybox=True)
plt.axhline(sys.mean(), linestyle='--', linewidth=0.5)
plt.axhline(dia.mean(), linestyle='--', linewidth=0.5)
plt.xticks([])

plt.show()
