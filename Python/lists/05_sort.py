my_tuple = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

sorted_tuple = sorted(my_tuple, key=lambda x: x[-1])

print("Sorted list of tuples (increasing order by last element):", sorted_tuple)