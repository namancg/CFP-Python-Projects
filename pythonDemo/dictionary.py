my_dict = {'name': 'Jack', 'age': 26}

# PRINTING NAME
print(my_dict['name'])

# PRINTING AGE
print(my_dict.get('age'))

# UPDATING IN A DICTIONARY
my_dict['age'] = 27
print(my_dict)

# ADDING INTO A DICTIONARY
my_dict['address'] = 'Downtown'
print(my_dict)

# POPPING FROM A DICTIONARY
my_dict.pop('age')
print(my_dict)

# PRINTING KEYS INSIDE A DICTIONARY
print(my_dict.keys())

# CLEARING A DICTIONARY
my_dict.clear()
print(my_dict)

