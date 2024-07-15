my_dict = {'a': 9, 'b':7, 'c':2}

sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item:item[1]))

sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item:item[1], reverse=True))

print(f"Sorted dictionary (ascending):  {sorted_dict_asc}")
print(f"Sorted dictionary (descending):  {sorted_dict_desc}")