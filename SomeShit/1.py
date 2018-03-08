import numpy as np
import matplotlib.pyplot as plt

# Create data
N = 5


x1 = np.array([1,1,2,2,3])
y1 = np.array([5,4,5,4,4])
g1 = (x1, y1)
g2 = (np.array([3,4,5,4,5]), np.array([1,1,1,2,2]))
g3 = (np.array([3]), np.array([2]))
data = (g1, g2, g3)

colors = ("red", "green", "black")
groups = ("Spinach", "Snacks", "Unknown")

# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, axisbg="1.0")

for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30)

plt.title('KNN example')
plt.xlabel('Spinach')
plt.ylabel('Scooby Snacks')
plt.legend(loc=2)
plt.show()