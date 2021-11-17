import numpy as np

x = np.arange(12).reshape(3, 4)
print("Original array elements:")
print(x)
for a in np.nditer(x, op_flags=['readwrite']):
    a[...] = 3 * a
print("New array elements:")
print(x)
