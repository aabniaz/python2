import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  
x = np.linspace(0.0, 0.6, 20)
y = x + np.random.normal(0, 0.05, size=len(x))  
plt.scatter(x, y, color='blue', marker='o')
plt.plot(x, x, color='red')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Best fit line using regression method')
plt.show()
