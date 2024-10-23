import numpy as np
import matplotlib.pyplot as plt

def rusanov_burstein_mirin(u, nu, v, omega, dx, dt, num_steps):
    N = len(u)
    u_new = np.zeros_like(u)
    
    for _ in range(num_steps):
        u_1 = 0.5 * (u[1:] + u[:-1]) - (1/3) * nu * (u[1:] - u[:-1])        
        u_2 = u[:-2] - (2/3) * nu * (u_1[1:] - u_1[:-1])
        omega = max(min(3, 4 * nu**2 - v**4), 4 * nu**2 - v**4)        
        u_new[2:-2] = u[2:-2] - (1/24) * nu * (-2*u[4:] + 7*u[3:-1] - 7*u[1:-3] + 2*u[:-4]) \
                      - (3/8) * nu * (u_2[2:] - u_2[:-2]) \
                      - (omega/24) * (u[4:] - 4*u[3:-1] + 6*u[2:-2] - 4*u[1:-3] + u[:-4])
        u_new[0] = u_new[-2]
        u_new[1] = u_new[-1]
        u_new[-1] = u_new[1]
        u_new[-2] = u_new[0]        
        u = np.copy(u_new)
    return u_new

nu = -0.1
v = 0.5
omega = 4 * nu**2 - v**4
dx = 0.1
dt = 0.01
num_steps = 100
u_initial = np.sin(np.linspace(0, 2*np.pi, 100))
u_final = rusanov_burstein_mirin(u_initial, nu, v, omega, dx, dt, num_steps)
plt.figure(figsize=(10, 5))
plt.plot(np.linspace(0, 2*np.pi, len(u_final)), u_final)
plt.xlabel('x')
plt.ylabel('u')
plt.legend()
plt.grid(True)
plt.show()
