def get_longest_word_length(word_list):
    longest_length = 0

    for word in word_list:
        if len(word) > longest_length:
            longest_length = len(word)

    return longest_length

word_list = ["apple", "banana", "cherry", "grapefruit", "kiwi"]

longest_length = get_longest_word_length(word_list)

print(f"Length of the longest word: {longest_length}")