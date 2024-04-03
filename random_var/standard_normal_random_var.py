import random

def generate_normal_variate_standard_normal(mu, sigma):
    u = random.random()
    z1, z2 = _get_interpolation_bounds(u)
    if z1 is None or z2 is None:
        return None  # Handle out-of-range case gracefully
    x = _linear_interpolation(u, z1, z2)
    return mu + sigma * x

def _get_interpolation_bounds(u):
    sorted_keys = sorted(_standard_normal_table.keys())
    min_key, max_key = sorted_keys[0], sorted_keys[-1]
    for key in sorted_keys:
        if key <= u:
            z1 = _standard_normal_table[key]
        else:
            z2 = _standard_normal_table[key]
            return z1, z2
    return min_key, max_key  # Return min and max values as default bounds

def _linear_interpolation(u, x1, x2):
    u1, u2 = sorted(_standard_normal_table.keys())
    return x1 + (u - u1) * (x2 - x1) / (u2 - u1)

# Table of standard normal distribution (example)
_standard_normal_table = {
    0.00: -2.326,
    0.01: -2.306,
    # Add more entries as needed
}

# Set parameters
mu = 0
sigma = 1

# Simulate 10 times
for _ in range(10):
    # Generate random variate
    x = generate_normal_variate_standard_normal(mu, sigma)
    if x is not None:
        # Print result if valid
        print(f"Random variate: {x}")
    else:
        print("Error: Random variate out of range")
