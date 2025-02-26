# Create a function to print all prime numbers up to n.
# Write a function to calculate the power of a number.


# prime which is divisible only by themselves:

def print_primes(n):
    for num in range(2, n + 1):  # Start from 2 (smallest prime)
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to √num
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")

n = 20
print_primes(n)  # Output: 2 3 5 7 11 13 17 19

''' The expression 29 ** 0.5 calculates the square root of 29:

29
≈
5.385
29
​
 ≈5.385  '''


n = 5

