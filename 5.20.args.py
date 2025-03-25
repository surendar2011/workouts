# Create a function that takes multiple arguments using *args.


# *args allows the function to accept any number of positional arguments.
def sum_numbers(*args):
    return sum(args)  # Sums all the arguments

# Example usage
result = sum_numbers(1, 2, 3, 4, 5)
print(result)  # Output: 15

