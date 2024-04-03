import random
import math

def generate_gamma_variate(alpha, beta):
    product = 1
    for _ in range(alpha):
        product *= random.random()
    return -math.log(product) / beta

# Set parameters
alpha = 2  # Shape parameter
beta = 0.5  # Scale parameter

# Simulate 10 times
for _ in range(10):
    # Generate random variate
    x = generate_gamma_variate(alpha, beta)

    # Print result
    print(f"Random variate (Gamma): {x}")
