def count_strings_with_same_first_and_last_char(strings_list):
    count = 0
    for string in strings_list:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

sample_list = ['abc', 'xyz', 'aba', '1221']

result = count_strings_with_same_first_and_last_char(sample_list)

print(f"Number of strings with same first and last character: {result}")