import numpy as np
import matplotlib.pyplot as plt

z = np.arange(-2, 2, 0.01)  # Define the range of x values

# Calculate the hinge loss
hinge = np.maximum(0, 1 - z)

# Calculate the squared loss
squared = (1 - z) ** 2

# Calculate the logistic loss
logistic = np.log(1 + np.exp(-z)) / np.log(2)

# Calculate the exponential loss
exponential = np.exp(-z)

# Calculate the zero-one loss
zero_one = (z < 0)

# Plot the loss functions
plt.figure()
plt.plot(z, hinge, '-r', linewidth=2)
plt.plot(z, squared * 2, '-g', linewidth=2)
plt.plot(z, logistic / np.log(2), '-b', linewidth=2)
plt.plot(z, exponential, '-k', linewidth=2)
plt.plot(z, zero_one, '-m', linewidth=2)
plt.legend(['Hinge Loss', 'Squared Loss', 'Logistic Loss', 'Exponential Loss', 'Zero-One Loss'])
plt.xlabel('z')
plt.ylabel('Loss')
plt.show()
