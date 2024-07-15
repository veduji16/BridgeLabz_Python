my_array = [10, 20, 30, 40, 50]

element_to_remove = 30
if element_to_remove in my_array:
    my_array.remove(element_to_remove)
    print(f"First occurrence of {element_to_remove} removed. Updated array:", my_array)
else:
    print(f"{element_to_remove} not found in the array.")