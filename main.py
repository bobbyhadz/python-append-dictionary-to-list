# Append a dictionary to a list in Python

my_dict = {'name': 'Alice', 'age': 30}

my_list = []

dict_copy = my_dict.copy() # 👈️ create copy

my_list.append(dict_copy)

print(my_list)  # 👉️ [{'name': 'Alice', 'age': 30}]