# Use the ternary operator to return a value.

# Syntax:
# value_if_true if condition else value_if_false

# Example 1: Find the Maximum of Two Numbers
a, b = 10, 20
max_value = a if a > b else b
print(max_value)  # Output: 20

# Example 2: Check if a Number is Even or Odd
num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(result)  # Output: Odd

# Example 4: Nested Ternary Operator
num = -5
result = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(result)  # Output: Negative
