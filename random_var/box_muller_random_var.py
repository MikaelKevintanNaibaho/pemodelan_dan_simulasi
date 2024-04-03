import numpy as np
import matplotlib.pyplot as plt

def box_muller_random_variable(size=1):
    # Generate random variables from standard normal distribution using Box-Muller method
    u1 = np.random.uniform(0, 1, size)
    u2 = np.random.uniform(0, 1, size)
    z0 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
    z1 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)
    return z0, z1

num_samples = 20
z_box_muller, _ = box_muller_random_variable(size=num_samples)

print("20 random varibale: ")
print(z_box_muller)
