# Generate Fibonacci numbers using a loop.

n = 10  # Number of Fibonacci numbers to generate
a, b = 0, 1

print("Fibonacci Sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b


# Output:
# Fibonacci Sequence:  
# 0 1 1 2 3 5 8 13 21 34  