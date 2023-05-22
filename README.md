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

# c) Plot and save
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

