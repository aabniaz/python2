import matplotlib.pyplot as plt
import numpy as np

def flower(num_petals=6, petal_length=1, radius=1):
    theta = np.linspace(0, 2*np.pi, 1000)    
    x_center, y_center = 0, 0
    petal = petal_length * np.sin(num_petals * theta)    
    x = radius * petal * np.cos(theta) + x_center
    y = radius * petal * np.sin(theta) + y_center    
    return x, y
x, y = flower(num_petals=6, petal_length=0.2, radius=1)
plt.figure(figsize=(8, 8))
plt.axis('equal')
plt.plot(x, y, color='red')
plt.show()
