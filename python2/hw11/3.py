import numpy
import matplotlib.pyplot as plt

x = numpy.linspace(0, 50, num=256)
a = numpy.sin(x * numpy.pi / 25)
b = numpy.cos(x * numpy.pi / 25)
c = numpy.sin(-x * numpy.pi / 25)
d = -numpy.cos(x * numpy.pi / 25)

plt.plot(x, a) #label='sin(x * π / 25)'
plt.plot(x, b) #label='cos(x * π / 25)'
plt.plot(x, c) #label='sin(-x * π / 25)'
plt.plot(x, d) #label='cos(-x * π / 25)'

plt.xlabel('')
plt.ylabel('')
#plt.legend()
plt.grid(True)
plt.show()
