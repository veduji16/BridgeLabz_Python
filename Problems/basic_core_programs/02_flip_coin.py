import random

def flip_coin(num_flips):
    if num_flips <= 0:
        print("Please enter a positive integer for the number of coin flips.")
        return

    heads_count = 0
    tails_count = 0

    for _ in range(num_flips):
        random_value = random.random()

        if random_value < 0.5:
            tails_count += 1
        else:
            heads_count += 1

    total_flips = heads_count + tails_count
    heads_percentage = (heads_count / total_flips) * 100
    tails_percentage = (tails_count / total_flips) * 100

    print(f"Number of coin flips: {total_flips}")
    print(f"Heads: {heads_count} ({heads_percentage:.2f}%)")
    print(f"Tails: {tails_count} ({tails_percentage:.2f}%)")

num_flips = int(input("Enter the number of times to flip the coin: "))
flip_coin(num_flips)