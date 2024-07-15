my_set = {1, 2, 3, 4, 5}

item_to_remove = 3

if item_to_remove in my_set:
    my_set.remove(item_to_remove)
    print(f"{item_to_remove} removed from the set.")
else:
    print(f"{item_to_remove} is not present in the set.")

print("Updated set:", my_set)