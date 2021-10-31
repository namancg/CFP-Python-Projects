import math
import random


def getLength(x1, x2, y1, y2):
    val = ((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1))
    result = math.sqrt(val)
    return result


x1 = random.random() * 100
x2 = random.random() * 100
y1 = random.random() * 100
y2 = random.random() * 100

x11 = random.random() * 100
x12 = random.random() * 100
y11 = random.random() * 100
y12 = random.random() * 100

l1 = getLength(x1, x2, y1, y2)
l2 = getLength(x11, x12, y11, y12)

print(l1)
print(l2)
if l1 == l2:
    print("BOTH ARE EQUAL")
elif l1 > l2:
    print("LINE 1 IS GREATER")
else:
    print("LINE 2 IS GREATER")
