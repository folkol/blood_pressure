import numpy as np
import matplotlib.pyplot as plt


def plot(title, data):
    plt.plot(data)
    plt.grid(True)
    plt.title(title, fontsize=20)
    sys = data[:, 0]
    dia = data[:, 1]
    plt.legend([
        '%s:\t${(min=%d, max=%d, mean=%d)}$' % ('SYS', sys.min(), sys.max(), sys.mean()),
        '%s:\t${(min=%d, max=%d, mean=%d)}$' % ('DIA', dia.min(), dia.max(), dia.mean())
    ], loc=2, fancybox=True)
    plt.axhline(sys.mean(), linestyle='--', linewidth=0.5, color='black')
    plt.axhline(dia.mean(), linestyle='--', linewidth=0.5, color='black')
    # plt.xticks([])
    plt.gca().axes.xaxis.set_ticklabels([])


readings = np.loadtxt('readings.dat', skiprows=1, usecols=(2, 3))

ax1 = plt.subplot(121)
plot('Morning', readings[::2])
plt.subplot(122, sharey=ax1)
plot('Evening', readings[1::2])

plt.show()
