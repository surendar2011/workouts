# Create a function to calculate the sum of squares.

def sum_of_squares(n):
    result = 0
    for i in range(1, n + 1):
        result += i ** 2  # Squaring each number
    return result

n = 3
print(sum_of_squares(n))  # Output: 14
