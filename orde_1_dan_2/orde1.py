import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the first-order differential equation
def first_order(y, t, k):
    dydt = -k * y  # dy/dt = -k * y
    return dydt

# Initial condition and time points
y0 = 1.0  # Initial condition
t = np.linspace(0, 10, 100)  # Time points

# System parameter (time constant)
k = 0.5

# Solve the differential equation
sol = odeint(first_order, y0, t, args=(k,))

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(t, sol[:, 0], 'b', label='y(t)')
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('First-Order System Response')
plt.legend(loc='best')
plt.grid()
plt.show()
