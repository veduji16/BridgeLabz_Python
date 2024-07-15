my_string = "google.com"

char_frequency = {}

for char in my_string:
    char_frequency[char] = char_frequency.get(char, 0) + 1

print("Character frequency:", char_frequency)