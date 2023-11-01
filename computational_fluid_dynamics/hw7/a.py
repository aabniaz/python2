import numpy as np
import matplotlib.pyplot as plt

k = 0.1  
delta_t = 1  
N = 10  
L = 10  

C3H8_initial = 1.0  
O2_constant = 10.0  
CO2_initial = 0.0    
H2O_initial = 0.0   

C3H8_concentrations = np.zeros((N,))  
O2_concentrations = np.full((N,), O2_constant)  
CO2_concentrations = np.zeros((N,))  
H2O_concentrations = np.zeros((N,))  

for t in range(0, 31, delta_t):
    for i in range(N):
        C3H8_concentrations[i] -= k * C3H8_concentrations[i] * O2_concentrations[i] * delta_t        
        CO2_concentrations[i] += (3 * k * C3H8_concentrations[i] * O2_concentrations[i] * delta_t) / 5
        H2O_concentrations[i] += (4 * k * C3H8_concentrations[i] * O2_concentrations[i] * delta_t) / 5
    
    if t in [0, 10, 20, 30]:
        plt.plot(np.linspace(0, L, N), C3H8_concentrations, label=f'Time: {t} seconds')

plt.xlabel('Distance along the pipe (meters)')
plt.ylabel('Concentration (mole/liter)')
plt.title('Concentration of C3H8 along the Pipe')
plt.legend()
plt.grid(True)
plt.show()
