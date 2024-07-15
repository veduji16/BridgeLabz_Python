import math

def euclidean_distance(x, y):
    return math.sqrt(x**2 + y**2)

x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

distance = euclidean_distance(x, y)

print(f"Euclidean distance from point ({x}, {y}) to the origin (0, 0) is {distance:.2f}")