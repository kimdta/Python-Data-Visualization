import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 99, 100)
y = np.random.randint(0, 200, 100)

print("linspace:", x)
print("random numbers", y)

# a) Create a scatter plot
plt.scatter(x, y, marker = "v")
plt.show()