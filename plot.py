import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('readings.dat', skiprows=1, usecols=(2, 3, 4))

morning = data[::2]
evening = data[1::2]

ax1 = plt.subplot(211)
plt.plot(morning)
plt.grid(True)
plt.title('Morning')
plt.legend([
    'SYS:\t(min=%d, max=%d, mean=%d)' % (13, 200, 45),
    'DIA:\t%d\t%d' % (30, 29),
    'HR:\t\t%d\t%d' % (3,1)
], loc=2, fancybox=True)
plt.xticks([])

plt.subplot(212, sharey=ax1)
plt.plot(evening)
plt.grid(True)
plt.title('Evening')
plt.legend([
    'SYS:\t(min=%d, max=%d, mean=%d)' % (13, 200, 45),
    'DIA:\t%d\t%d' % (30, 29),
    'HR:\t\t%d\t%d' % (3,1)
], loc=2, fancybox=True)
plt.xticks([])

plt.show()
