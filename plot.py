import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('readings.dat', skiprows=1, usecols=(2, 3))

morning = data[::2]
evening = data[1::2]

ax1 = plt.subplot(121)
plt.plot(morning)
plt.grid(True)
plt.title('Morning')
sys = morning[:, 0]
dia = morning[:, 1]
plt.legend([
    'SYS:\t${(min=%5.d, max=%d, mean=%d)}$' % (sys.min(), sys.max(), sys.mean()),
    'DIA:\t${(min=%d, max=%d, mean=%d)}$' % (dia.min(), dia.max(), dia.mean())
], loc=2, fancybox=True)
xlim = ax1.get_xlim()
plt.hlines(dia.mean(), xlim[0], xlim[1], linestyles='--')
plt.hlines(sys.mean(), xlim[0], xlim[1], linestyles='--')
plt.xticks([])

plt.subplot(122, sharey=ax1)
plt.plot(evening)
plt.grid(True)
plt.title('Evening')
sys = evening[:, 0]
dia = evening[:, 1]
plt.legend([
    'SYS:\t${(min=%5.d, max=%d, mean=%d)}$' % (sys.min(), sys.max(), sys.mean()),
    'DIA:\t${(min=%d, max=%d, mean=%d)}$' % (dia.min(), dia.max(), dia.mean())
], loc=2, fancybox=True)
plt.xticks([])
xlim = ax1.get_xlim()
plt.hlines(sys.mean(), xlim[0], xlim[1], linestyles='--')
plt.hlines(dia.mean(), xlim[0], xlim[1], linestyles='--')

plt.show()
