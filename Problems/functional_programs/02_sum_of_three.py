def find_triplets(arr):
    triplets = set()

    arr.sort()

    for i in range(len(arr)):
        left, right = i + 1, len(arr) - 1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == 0:
                triplets.add((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return triplets

N = int(input("Enter the number of integers (N): "))
arr = []
for i in range(N):
    arr.append(int(input(f"Enter integer {i + 1}: ")))

triplets = find_triplets(arr)

print(f"Number of distinct triplets that sum to zero: {len(triplets)}")

print("Distinct triplets:")
for triplet in triplets:
    print(triplet)