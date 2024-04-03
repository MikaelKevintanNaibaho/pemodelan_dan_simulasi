import numpy as np
import matplotlib.pyplot as plt

def weibull_random_variable(k, lambd, size=1):
    # Generate random variables from the Weibull distribution using inverse transform method
    u = np.random.uniform(0, 1, size)
    x = lambd * (-np.log(1 - u))**(1/k)
    return x

def untung_rugi_random_variable(num_simulations, mean, std_dev):
    # Generate random variate for profit-loss scenario using normal distribution
    return np.random.normal(mean, std_dev, num_simulations)

def box_muller_random_variable(size=1):
    # Generate random variables from standard normal distribution using Box-Muller method
    u1 = np.random.uniform(0, 1, size)
    u2 = np.random.uniform(0, 1, size)
    z0 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
    z1 = np.sqrt(-2 * np.log(u1)) * np.sin(2 * np.pi * u2)
    return z0, z1

def central_limit_random_variable(distribution_func, num_samples, sample_size):
    # Generate random variables using Central Limit Theorem (CLT)
    samples_sum = np.sum(distribution_func(size=(num_samples, sample_size)), axis=1)
    z = (samples_sum - np.mean(samples_sum)) / np.std(samples_sum)
    return z

def standard_normal_random_variable(mean, variance, size=1):
    # Generate random variables from normal distribution with given mean and variance
    x = np.random.normal(mean, np.sqrt(variance), size)
    z = (x - mean) / np.sqrt(variance)
    return z

# Parameters for normal distribution
mean_untung_rugi = 3000000  # Mean untuk persoalan untung-rugi
std_dev_untung_rugi = 1500000  # Standar deviasi untuk persoalan untung-rugi

# Simulate random variables for Weibull distribution
k = 2.5
lambd = 3
num_samples_weibull = 1000
weibull_samples = weibull_random_variable(k, lambd, num_samples_weibull)

# Simulate random variate for profit-loss scenario using normal distribution
num_simulations = 20
untung_rugi_samples = untung_rugi_random_variable(num_simulations, mean_untung_rugi, std_dev_untung_rugi)

# Cetak 20 random variate dari distribusi normal untuk persoalan untung-rugi
print("20 Random Variate dari Persoalan Untung-Rugi (Distribusi Normal):")
print(untung_rugi_samples)


# Simulate random variables using different methods for normal distribution
num_samples_normal = 1000
sample_size_clt = 100
z_box_muller, _ = box_muller_random_variable(size=num_samples_normal)
z_clt = central_limit_random_variable(np.random.uniform, num_samples_normal, sample_size_clt)
z_standard_normal = standard_normal_random_variable(mean=mean_untung_rugi, variance=std_dev_untung_rugi**2, size=num_samples_normal)

# Plot histograms of simulated random variables
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.hist(weibull_samples, bins=30, density=True, alpha=0.6, color='g')
plt.title('Weibull Distribution')
plt.xlabel('Random Variable Value')
plt.ylabel('Probability Density')

plt.subplot(2, 3, 2)
plt.hist(untung_rugi_samples, bins=10, density=True, alpha=0.6, color='b')
plt.title('Profit-Loss Scenario (Normal Distribution)')
plt.xlabel('Random Variable Value')
plt.ylabel('Probability Density')

plt.subplot(2, 3, 3)
plt.hist(z_box_muller, bins=30, density=True, alpha=0.6, color='b')
plt.title('Box-Muller Method')
plt.xlabel('Random Variable Value')
plt.ylabel('Probability Density')

plt.subplot(2, 3, 4)
plt.hist(z_clt, bins=30, density=True, alpha=0.6, color='g')
plt.title('Central Limit Theorem (CLT)')
plt.xlabel('Random Variable Value')
plt.ylabel('Probability Density')

plt.subplot(2, 3, 5)
plt.hist(z_standard_normal, bins=30, density=True, alpha=0.6, color='r')
plt.title('Standard Normal Method')
plt.xlabel('Random Variable Value')
plt.ylabel('Probability Density')

plt.tight_layout()
plt.show()
