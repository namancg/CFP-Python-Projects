"""Write a Python program to draw a scatter plot with empty circles taking a random distribution
in X and Y and plotted against each other."""
import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(50)
y = np.random.randn(50)
plt.scatter(x, y, s=70, facecolors='none', edgecolors='g')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
