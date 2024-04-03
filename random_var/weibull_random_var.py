import numpy as np
import matplotlib.pyplot as plt

def weibull_random_variable(k, lambd, size=1):
    # Generate random variables from the Weibull distribution using inverse transform method
    u = np.random.uniform(0, 1, size)
    x = lambd * (-np.log(1 - u))**(1/k)
    return x


# Simulate random variables for Weibull distribution
k = 2.5
lambd = 3
num_samples_weibull = 20
weibull_samples = weibull_random_variable(k, lambd, num_samples_weibull)

print("20 random varibale: ")
print(weibull_samples)