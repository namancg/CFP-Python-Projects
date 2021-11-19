fruit_list = ['apple', 'mango', 'carrot', 'banana']

# LENGTH OF A LIST
print("LENGTH OF THE LIST")
print(len(fruit_list))

# APPENDING TO A LIST
fruit_list.append("strawberry")
print(fruit_list)

# REMOVING FROM A LIST
fruit_list.remove("strawberry")
print(fruit_list)

# SORTING A LIST
fruit_list.sort()
print("SORTED FRUIT LIST", fruit_list)

# EXTENDING A LIST
fruit_list.extend(["strawberry", "Kiwi"])
print(fruit_list)

# POPPING FROM THE LIST
fruit_list.pop(4)
print(fruit_list)

# SLICE IN A LIST
print(fruit_list[:5])
print(fruit_list[1:5])
print(fruit_list[2:4])

# REVERSE A LIST
print(fruit_list)
fruit_list.reverse()
print(fruit_list)

# COUNTING IN A LIST
print(fruit_list.count("Kiwi"))

# CONCATENATING A LIST
new_vegetable_list = ["BEANS", "BROCCOLI"]
print(fruit_list + new_vegetable_list)

# CLEAR A LIST
fruit_list.clear()
print(fruit_list)
