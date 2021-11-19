tuple1 = ('physics', 'chemistry', 1997, 2000);
tuple2 = (1, 2, 3, 4, 5);
tuple3 = "a", "b", "c", "d";

# ADDING/CONCATENATING TWO TUPLES
temp_tuple = tuple3 + tuple2
print(temp_tuple)

# DELETING TUPLE ELEMENTS
del tuple1
# REPETITION IN A TUPLE
print(tuple2 * 4)

# CHECKING IF AN ELEMENT IS PRESENT
print(3 in tuple2)

# ITERATION IN TUPLE
for x in tuple2:
    print(x)

# SLICING IN TUPLE
print(tuple2[3])
print(tuple2[1:])

print(max(tuple2))
print(min(tuple2))

my_list = ["hello", 123]
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)
