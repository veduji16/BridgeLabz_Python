def print_powers_of_2(N):
    if N < 0 or N >= 31:
        print("Please enter a valid value for N (0 <= N < 31).")
        return

    for i in range(N + 1):
        power_of_2 = 2 ** i
        print(f"2^{i} = {power_of_2}")

N = int(input("Enter the power value N (0 <= N < 31): "))
print_powers_of_2(N)
