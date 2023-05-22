# Python-Data-Visualization

# 1. Line Chart
a) Create 2 numpy arrays "time" and "dist"
```ruby
import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0,11)        #time-array with numbers from 0 to 10
dist = np.zeros(shape=(11))   #1 dimensional array - with 11 zeros
#dist = np.zeros((11))

print(time)
print(dist)
```
===> [ 0  1  2  3  4  5  6  7  8  9 10]
    [0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

b) Fill the dist-array with the result of following function: d= 0.5*9.81*s^2 
```ruby
i = 0
for s in time:
    dist[i] = 0.5 * 9.81 * np.power(s, 2) 
    i += 1
print(dist)
```
===> [  0.  4.905  19.62   44.145  78.48  122.625 176.58  240.345 313.92 397.305 490.5  ]

c) Plot and save
```ruby
plt.plot(time, dist, ".g", label = 'd')
plt.title("Fallen Distance")
plt.xlabel("time[s] after release")
plt.ylabel("distance[m]")
plt.legend(loc ="upper left")
plt.savefig('./Figure.png') #save it in current directory
plt.show()
```
![Figure](https://github.com/kimdta/Python-Data-Visualization/assets/133651115/60084c70-1752-40f3-9abf-7e19a8e0554f)

d) Change the background color of the plot
```ruby
ax = plt.gca()
ax.set_facecolor("#EAF5F8")

plt.savefig('./Figure.png') 
plt.show()
```
![Figure](https://github.com/kimdta/Python-Data-Visualization/assets/133651115/033cd8f9-3b7a-4887-aa9a-4ce1ce48d573)

# 2. Scatter Plot
Create a scatter plot from two arrays:
```ruby
x = np.linspace(0, 99, 100)
y = np.random.randint(0, 200, 100)

print("linspace:", x)
print("random numbers", y)

plt.scatter(x, y, marker = "v")
plt.show()
```
![Scatter plot](https://github.com/kimdta/Python-Data-Visualization/assets/133651115/9df600ce-5b36-436e-a82f-e7f5b552f01d)

# 3. Bar chart
Create a bar chart from two arrays:
```ruby
x = ["1²", "2²", "3²"]
y = np.arange(1, 4)**2  

plt.bar(x, y)
plt.show()
```
![Bar chart](https://github.com/kimdta/Python-Data-Visualization/assets/133651115/1d7e9f81-63c2-445d-9b5f-a9e6eed62584)

# 4. Box Plot
From matplotlib.patches import Polygon
```ruby
import numpy as np
import matplotlib.pyplot as plt

values_low = np.random.randint(70, 80, 10)
values_mid = np.random.randint(80, 120, (100))
values_high = np.random.randint(120, 130, (10))

print("values_low:", values_low) ---> values_low: [70 73 75 76 78 77 76 72 72 72]
print("values_mid:", values_mid) ---> values_mid: [ 81  99 118  95 115  94 115 ... 119  96 101 117 115  86]
print("values_high:", values_high) ---> values_high: [125 120 126 127 124 127 129 126 128 129]

values_all = np.concatenate((values_low, values_mid, values_high))
```
Create a box plot

```ruby
plt.boxplot(values_all)
# Alternative
# figure, axes = plt.subplots()
# axes.boxplot(values_all)

plt.savefig("./Boxplot.png")

min = values_all.min()
p25 = np.percentile(values_all, 25)
p50 = np.percentile(values_all, 50)
p75 = np.percentile(values_all, 75) 
max = values_all.max()

print("Min:" + str(min) + " P25:" + str(p25) + " P50:" + str(p50) + " P75:" + str(p75) + " Max:" + str(max))
plt.show()
```
===> Min:70 P25:85.0 P50:95.5 P75:109.0 Max:129
![Box plot](https://github.com/kimdta/Python-Data-Visualization/assets/133651115/23da5507-c5cb-4b85-b8ed-e874de980934)

