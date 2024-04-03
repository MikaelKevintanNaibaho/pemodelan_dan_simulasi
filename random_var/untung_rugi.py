from uniform_random_var import generate_uniform_variate

a = -4000000
b = 10000000

# Simulate random variate 20 times
n = 20
profit_loss_list = [generate_uniform_variate(a, b) for _ in range(n)]

# Print simulation results
for idx, profit_loss in enumerate(profit_loss_list, 1):
    print(f"Month {idx}: Rp. {profit_loss:,.2f}")
