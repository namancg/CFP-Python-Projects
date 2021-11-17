import numpy as np

a = np.array([[0, 1, 3], [5, 7, 9]])
print(a)
b = np.array([[0, 2, 4], [6, 8, 10]])
print(b)
c = np.concatenate((a, b), 1)
print(c)
