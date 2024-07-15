def compute_harmonic_number(N):
    if N == 0:
        print("N must be a non-zero positive integer.")
        return

    harmonic_sum = 0
    for i in range(1, N + 1):
        harmonic_sum += 1 / i

    return harmonic_sum

N = int(input("Enter the harmonic value N (non-zero positive integer): "))
harmonic_value = compute_harmonic_number(N)
print(f"The {N}th harmonic value is approximately {harmonic_value:.6f}")