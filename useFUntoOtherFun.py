# Write a function that takes another function as an argument.

def apply_function(func, values):
    return [func(i) for i in values]  # Apply `func` to each element

# Function to square a number
def square(num):
    return num ** 2

numbers = [1, 2, 3, 4]

# Passing `square` function as an argument
result = apply_function(square, numbers)

print(result)  # Output: [1, 4, 9, 16]