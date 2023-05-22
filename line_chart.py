import numpy as np
import matplotlib.pyplot as plt

# a) Create 2 numpy arrays "time" and "dist"
time = np.arange(0,11)        #time-array with numbers from 0 to 10
dist = np.zeros(shape=(11))   #1 dimensional array - with 11 zeros
#dist = np.zeros((11))

# print(time)
# print(dist)

# b) Fill the dist-array with the result of following function: d= 0.5*9.81*s^2 
i = 0
for s in time:
    dist[i] = 0.5 * 9.81 * np.power(s, 2) 
    i += 1
print(dist)

# c) Plot and save
plt.plot(time, dist, ".g", label = 'd')
plt.title("Fallen Distance")
plt.xlabel("time[s] after release")
plt.ylabel("distance[m]")
plt.legend(loc ="upper left")
plt.savefig('./Figure.png') #save it in current directory
#plt.show()

# d) Change the background color of the plot
ax = plt.gca()
ax.set_facecolor("#EAF5F8")

plt.savefig('./Figure.png') 
plt.show()

