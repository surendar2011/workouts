# Print all prime numbers from 1 to 50.

for num in range(1, 51):  # Iterate from 1 to 50
    if num > 1:  # Prime numbers are greater than 1
        for i in range(2, int(num ** 0.5) + 1):  # Check divisibility from 2 to sqrt(num)
            if num % i == 0:
                break  # Not a prime, exit the loop
        else:
            print(num, end=" ")  # Print prime number

# Output:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
