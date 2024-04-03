import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt



# Define the second-order differential equation
def second_order(y, t, zeta, wn):
    y1, y2 = y
    dydt = [y2, -2 * zeta * wn * y2 - wn**2 * y1]  # dy1/dt = y2, dy2/dt = -2*zeta*wn*y2 - wn^2*y1
    return dydt

# Initial conditions and time points
y0 = [1.0, 0.0]  # Initial conditions for y1 and y2
t = np.linspace(0, 10, 100)  # Time points

# System parameters
zeta = 0.5  # Damping ratio
wn = 1.0    # Natural frequency

# Solve the differential equation
sol = odeint(second_order, y0, t, args=(zeta, wn))

# Extract the responses
y1 = sol[:, 0]
y2 = sol[:, 1]

# Plot the results
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, y1, 'b', label='y1(t)')
plt.xlabel('Time')
plt.ylabel('y1(t)')
plt.title('Second-Order System Response')
plt.legend(loc='best')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, y2, 'g', label='y2(t)')
plt.xlabel('Time')
plt.ylabel('y2(t)')
plt.legend(loc='best')
plt.grid()

plt.tight_layout()
plt.show()
