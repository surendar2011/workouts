# Create a tuple of all even numbers from 1 to 10.

even_numbers = tuple(i for i in range(1, 11) if i % 2 == 0)
print(even_numbers)

# Output:
# (2, 4, 6, 8, 10)