import random

def generate_normal_variate_clt(mu, sigma, n):
  u = [random.random() for _ in range(n)]
  x = sum(u) / n
  return mu + sigma * (x - 0.5)

# Set parameter
mu = 0
sigma = 1

# Simulate 10 times
for _ in range(10):
  # Generate random variate
  x = generate_normal_variate_clt(mu, sigma, 12)

  # Print result
  print(f"Random variate: {x}")
