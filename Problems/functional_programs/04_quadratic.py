import math

def calculate_quadratic_roots(a, b, c):
    delta = b**2 - 4*a*c

    if delta > 0:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        return root1, root2
    elif delta == 0:
        root = -b / (2*a)
        return root, root
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(delta)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

root1, root2 = calculate_quadratic_roots(a, b, c)

print(f"Root 1 of x: {root1:.2f}")
print(f"Root 2 of x: {root2:.2f}")