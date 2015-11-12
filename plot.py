import pylab

data=pylab.loadtxt('readings', usecols=(2,3,4))
pylab.plot(data)
pylab.show()
