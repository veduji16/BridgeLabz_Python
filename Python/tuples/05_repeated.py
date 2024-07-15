def find_repeated_items(my_tuple):
    repeated_items = set()
    seen_items = set()

    for item in my_tuple:
        if item in seen_items:
            repeated_items.add(item)
        else:
            seen_items.add(item)

    return repeated_items

my_tuple = (1, 2, 3, 2, 4, 5, 4, 6, 7, 7)

result = find_repeated_items(my_tuple)

print("Repeated items in the tuple:", result)