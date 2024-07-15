def read_2d_array(rows, cols):
    array_2d = []

    for i in range(rows):
        row = input(f"Enter {cols} space-separated values for row {i + 1}: ")
        row_values = row.split()
        if len(row_values) != cols:
            print(f"Error: Expected {cols} values for row {i + 1}, but received {len(row_values)} values.")
            return None
        array_2d.append(row_values)

    return array_2d

def print_2d_array(array_2d):
    if array_2d:
        for row in array_2d:
            print(" ".join(row))
    else:
        print("Error: Invalid 2D array.")

M = int(input("Enter the number of rows (M): "))
N = int(input("Enter the number of columns (N): "))

array_2d = read_2d_array(M, N)

print("\n2D Array:")
print_2d_array(array_2d)