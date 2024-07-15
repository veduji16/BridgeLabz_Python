my_string = 'restart'

modified_string = my_string[0] + my_string[1:].replace(my_string[0], '$')

print("Modified string:", modified_string)