import random

def generate_distinct_coupons(N):
    distinct_coupons = set()
    total_random_numbers = 0

    while len(distinct_coupons) < N:
        random_number = random.randint(1, N)  
        total_random_numbers += 1

        if random_number not in distinct_coupons:
            distinct_coupons.add(random_number)

    return total_random_numbers

N = int(input("Enter the number of distinct coupon numbers (N): "))

total_random_numbers_needed = generate_distinct_coupons(N)

print(f"Total random numbers needed to have all {N} distinct coupon numbers: {total_random_numbers_needed}")