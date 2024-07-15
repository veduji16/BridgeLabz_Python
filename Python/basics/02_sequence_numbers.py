user_input = input("Enter comma-separated numbers: ")

number_list = user_input.split(",")

number_tuple = tuple(number_list)

print("List:", number_list)
print("Tuple:", number_tuple)