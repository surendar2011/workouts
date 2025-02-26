# Create a function that takes a lambda function as an argument.


'''
square = lambda x: x ** 2
print(square(5))  # Output: 25


Here, lambda x: x ** 2 is the same as:

def square(x):
    return x ** 2

add = lambda a, b: a + b
print(add(3, 7))  # Output: 10

def add(a, b):
    return a + b


'''

def apply_lambda(func, values):
    return [func(x) for x in values]  # Apply the lambda function to each element

numbers = [1, 2, 3, 4]

# Passing a lambda function to square each number
result = apply_lambda(lambda x: x ** 2, numbers)

print(result)  # Output: [1, 4, 9, 16]
