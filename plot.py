import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('readings.dat', skiprows=1, usecols=(2, 3))


def plot(title, data):
    plt.plot(data)
    plt.grid(True)
    plt.title(title, fontsize=20)
    sys = data[:, 0]
    dia = data[:, 1]
    plt.legend([
        'SYS:\t${(min=%5.d, max=%d, mean=%d)}$' % (sys.min(), sys.max(), sys.mean()),
        'DIA:\t${(min=%d, max=%d, mean=%d)}$' % (dia.min(), dia.max(), dia.mean())
    ], loc=2, fancybox=True)
    plt.axhline(sys.mean(), linestyle='--', linewidth=0.5)
    plt.axhline(dia.mean(), linestyle='--', linewidth=0.5)
    # plt.xticks([])
    plt.gca().axes.xaxis.set_ticklabels([])


ax1 = plt.subplot(121)
plot('Morning', data[::2])
plt.subplot(122, sharey=ax1)
plot('Evening', data[1::2])

plt.show()
