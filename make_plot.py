import os
import matplotlib.pyplot as plt

# Get the absolute path of the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the data file
data_file_path = os.path.join(script_dir, "build/bin/L_t_data.txt")

# Read data from file
data = []
with open(data_file_path, "r") as file:
    for line in file:
        time, l_value = map(float, line.strip().split())
        data.append((time, l_value))

# Extract time and L(t) values
times, l_values = zip(*data)

# Create the plot
plt.plot(times, l_values)
plt.xlabel("Simulation Time (t)")
plt.ylabel("Number of Customers (L(t))")
plt.title("L(t) vs. Simulation Time")
plt.grid(True)
plt.show()
