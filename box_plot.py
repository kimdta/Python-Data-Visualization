import numpy as np
import matplotlib.pyplot as plt
# from matplotlib.patches import Polygon

values_low = np.random.randint(70, 80, 10)
values_mid = np.random.randint(80, 120, (100))
values_high = np.random.randint(120, 130, (10))

print("values_low:", values_low)

print("values_mid:", values_mid)

print("values_high:", values_high)

values_all = np.concatenate((values_low, values_mid, values_high))
print("values_all:", values_all)

# c) Create a box plot
# figure, axes = plt.subplots()
# axes.boxplot(values_all)

# or alternative
plt.boxplot(values_all) 
plt.savefig("./Boxplot.png")

min = values_all.min()
p25 = np.percentile(values_all, 25)
p50 = np.percentile(values_all, 50)
p75 = np.percentile(values_all, 75) 
max = values_all.max()

print("Min:" + str(min) + " P25:" + str(p25) + " P50:" + str(p50) + " P75:" + str(p75) + " Max:" + str(max))
plt.show()