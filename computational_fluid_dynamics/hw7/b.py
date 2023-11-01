import numpy as np
import matplotlib.pyplot as plt

delta_t_optimal_k = 1  
N_optimal_k = 10  
L_optimal_k = 10  
O2_constant_optimal_k = 10.0  
CO2_threshold_optimal_k = 0.01  

max_k = 1.0  
k_step = 0.01  
optimal_k = None

while max_k >= 0.0:
    C3H8_concentrations = np.zeros((N_optimal_k,))  
    O2_concentrations = np.full((N_optimal_k,), O2_constant_optimal_k)  
    CO2_concentrations = np.zeros((N_optimal_k,))  
    H2O_concentrations = np.zeros((N_optimal_k,))  
    for t in range(0, 101, delta_t_optimal_k):  
        for i in range(N_optimal_k):
            C3H8_concentrations[i] -= max_k * C3H8_concentrations[i] * O2_concentrations[i] * delta_t_optimal_k            
            CO2_concentrations[i] += (3 * max_k * C3H8_concentrations[i] * O2_concentrations[i] * delta_t_optimal_k) / 5
            H2O_concentrations[i] += (4 * max_k * C3H8_concentrations[i] * O2_concentrations[i] * delta_t_optimal_k) / 5
        
        if CO2_concentrations[-1] < CO2_threshold_optimal_k:
            optimal_k = max_k
            break
    
    max_k -= k_step

print("Optimal k for reagents not reaching the right side:", optimal_k)

time_points = [0, 10, 20, 30]  

C3H8_concentrations = np.zeros((N_optimal_k,)) 
O2_concentrations = np.full((N_optimal_k,), O2_constant_optimal_k)  
CO2_concentrations = np.zeros((N_optimal_k,)) 
H2O_concentrations = np.zeros((N_optimal_k,)) 

for t in range(0, 31, delta_t_optimal_k):
    for i in range(N_optimal_k):
        C3H8_concentrations[i] -= optimal_k * C3H8_concentrations[i] * O2_concentrations[i] * delta_t_optimal_k        
        CO2_concentrations[i] += (3 * optimal_k * C3H8_concentrations[i] * O2_concentrations[i] * delta_t_optimal_k) / 5
        H2O_concentrations[i] += (4 * optimal_k * C3H8_concentrations[i] * O2_concentrations[i] * delta_t_optimal_k) / 5
    
    if t in time_points:
        plt.plot(np.linspace(0, L_optimal_k, N_optimal_k), C3H8_concentrations, label=f'Time: {t} seconds')

plt.xlabel('Distance along the space (meters)')
plt.ylabel('Concentration (mole/liter)')
plt.title('Concentration of C3H8 along the Space')
plt.legend()
plt.grid(True)
plt.show()
