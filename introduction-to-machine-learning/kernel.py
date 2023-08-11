import numpy as np
import matplotlib.pyplot as plt

# Define the range of values for x
x_range = np.linspace(-5, 5, 10)

# Compute the kernel values k(x, x') = x * x' for each value of x
kernel_values = x_range * x_range[:, np.newaxis]

# Create the plot
plt.figure(figsize=(6, 6))
plt.imshow(kernel_values, extent=(-5, 5, -5, 5), origin='lower', cmap='viridis')
plt.colorbar(label='k(x, x\') = x * x\'')
plt.xlabel('x')
plt.ylabel('x\'')
plt.title('Kernel Plot: k(x, x\') = x * x\'')
plt.show()
