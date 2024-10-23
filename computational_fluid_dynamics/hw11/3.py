#not correct

import numpy as np
import matplotlib.pyplot as plt

def solve_hyperbolic_equation(u_initial, nu, omega, dx, dt, num_steps):
    # Initialize the solution array
    N = len(u_initial)
    u = np.zeros((num_steps, N))
    u[0, :] = u_initial

    # Time-stepping loop
    for n in range(1, num_steps):
        # Step 1
        u[n, 0] = u[n-1, 0] - (2/3) * nu * (u[n-1, 1] - u[n-1, 0])

        # Step 2
        u[n, 1] = 0.5 * (u[n-1, 0] + u[n-1, 1]) - (2/3) * nu * (u[n-1, 1] - u[n-1, 0])

        # Step 3
        u[n, 2:] = u[n-1, 2:] - (1/24) * nu * (-2*u[n-1, 4:] + 7*u[n-1, 3:-1] - 7*u[n-1, 1:-3] + 2*u[n-1, :-4]) \
                    - (3/8) * nu * (u[n-1, 2:] - u[n-1, 1:-1]) \
                    - (omega/24) * (u[n-1, 4:] - 4*u[n-1, 3:-1] + 6*u[n-1, 2:-2] - 4*u[n-1, 1:-3] + u[n-1, :-4])

    return u

# Example usage
nu = -0.1
omega = 4 * nu**2
dx = 0.1
dt = 0.01
num_steps = 100

# Initial condition (you may modify this according to your problem)
u_initial = np.sin(np.linspace(0, 2*np.pi, 100))

# Solve the hyperbolic equation
u_solution = solve_hyperbolic_equation(u_initial, nu, omega, dx, dt, num_steps)

# Plot the results
plt.figure(figsize=(10, 5))
for n in range(num_steps):
    plt.plot(np.linspace(0, 2*np.pi, len(u_solution[n])), u_solution[n], label=f'Step {n}')

plt.title('Hyperbolic Equation Solution')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.legend()
plt.grid(True)
plt.show()
