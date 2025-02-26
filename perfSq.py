import math

def is_perfect_square(n):
    if n < 0:
        return False  # Negative numbers can't be perfect squares
    
    sqrt_n = math.isqrt(n)  # Get the integer square root
    return sqrt_n * sqrt_n == n  # Check if it squares back to n

# Example usage
print(is_perfect_square(25))  # Output: True (5*5 = 25)
print(is_perfect_square(26))  # Output: False (no integer * itself gives 26)
