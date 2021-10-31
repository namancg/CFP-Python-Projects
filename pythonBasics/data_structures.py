# Lists
my_list = []  # create empty list
print(my_list)
my_list = [1, 2, 3, 'example', 3.132]  # creating list with data
print(my_list)
print(my_list[3])  # access index 3 element
print(my_list[0:2])  # access elements from 0 to 1 and exclude 2

# Dictionaries
my_dict = {}  # empty dictionary
print(my_dict)
my_dict = {'First': 'Python', 'Second': 'Java'}  # dictionary with elements
print(my_dict)
print(my_dict['First'])  # access elements using keys
print(my_dict.get('Second'))

# Tuples
my_tuple = (1, 2, 3, ['hindi', 'python'])  # create tuple
print(my_tuple)
print(my_tuple.count(2))

# Sets
my_set = {1, 2, 3}
my_set.add(4)  # add element to set
print(my_set)
my_set.clear()
print(my_set)
my_set = {1, 2, 3, 4}
my_set_2 = {3, 4, 5, 6}
print(my_set.union(my_set_2), '----------', my_set | my_set_2)
print(my_set.intersection(my_set_2), '----------', my_set & my_set_2)
print(my_set.difference(my_set_2), '----------', my_set - my_set_2)
print(my_set.symmetric_difference(my_set_2), '----------', my_set ^ my_set_2)
