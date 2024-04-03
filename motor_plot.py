import numpy as np
import matplotlib.pyplot as plt

# Load the data
data = np.loadtxt('motor_data.txt')  # Replace 'your_data_file.txt' with the actual file name

# Extract x, y, z coordinates
x = data[:, 0]
y = data[:, 1]
z = data[:, 2]

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.title('Scatter plot of XYZ coordinates')
plt.show()
