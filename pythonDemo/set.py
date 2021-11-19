my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# DIFFERENTIATING BETWEEN SET AND DICT
a = {}
b = set()
print(type(a))
print(type(b))

# ADDING TO A SET
my_set.add(2)
print(my_set)

# UPDATING A SET
my_set.update([2, 3, 4])
print(my_set)

my_set.discard(4)
print(my_set)

my_set.remove(1.0)
print(my_set)

my_set.clear()
print(my_set)

# SET OPERATIONS
# UNION
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A | B)

C = A.union(B)
D = B.union(A)
print(C)
print(D)

# INTERSECTION
print(A & B)
print(A.intersection(B))
print(B.intersection(A))

# DIFFERENCE
print(A - B)
print(A.difference(B))
print(B.difference(A))

# SYMMETRIC DIFFERENCE
print(A ^ B)
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

