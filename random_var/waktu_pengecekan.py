from exponen_random_var import generate_exponential_variates

def linear_congruential_generator(seed, a, m, n):
    random_numbers = []
    x = seed
    for _ in range(n):
        x = (a * x) % m
        random_numbers.append(x / m)  # Normalized random number between 0 and 1
    return random_numbers



# Parameter simulasi
seed = 12357
a = 173
m = 1237
n = 20  # Jumlah sampel
lambd = 0.1  # Rate parameter distribusi eksponensial

# Generate random numbers
random_numbers = linear_congruential_generator(seed, a, m, n)

# Generate exponential variates
exponential_variates = generate_exponential_variates(random_numbers, lambd)

# Hitung waktu total pengecekan
total_time = sum(exponential_variates)
print(f"Total waktu pengecekan: {total_time} menit")


# Simulasi pengecekan berurut
total_time_seq = 0
for time in exponential_variates:
    total_time_seq += time

print(f"Total waktu pengecekan berurut: {total_time_seq} menit")
