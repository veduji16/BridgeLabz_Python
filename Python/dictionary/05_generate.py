def generate_squared_dict(n):
    result_dict = {}
    
    for x in range(1, n + 1):
        result_dict[x] = x * x
    
    return result_dict

n = 5

squared_dict = generate_squared_dict(n)

print("Generated dictionary:", squared_dict)