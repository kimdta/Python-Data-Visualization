import numpy as np
import matplotlib.pyplot as plt

x = ["1²", "2²", "3²"]
y = np.arange(1, 4)**2  

print(x, y)

# b) Create a bar chart
plt.bar(x, y)
plt.show()