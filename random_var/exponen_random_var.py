import random
import math

def linear_congruential_generator(seed, a, m, n):
    random_numbers = []
    x = seed
    for _ in range(n):
        x = (a * x) % m
        random_numbers.append(x / m)  # Normalized random number between 0 and 1
    return random_numbers


def generate_exponential_variates(random_numbers, lambd):
    variates = []
    for rand_num in random_numbers:
        x = -math.log(1 - rand_num) / lambd
        variates.append(x)
    return variates

seed = 12357
a = 173
m = 1237
n = 20  # Jumlah sampel
lambd = 0.5  # Rate parameter

# Simulate 10 times
for simulation in range(10):
    random_numbers = linear_congruential_generator(seed + simulation, a, m, n)
    # Generate random variate
    x = generate_exponential_variates(random_numbers, lambd)

    # Print result
    print(f"Simulation {simulation+1}: Random variate (Exponential): {x}")
