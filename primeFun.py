# Write a function to check if a number is prime.

'''
# Define a function named 'is_prime' that takes one argument 'n'
def is_prime(n):
    # Docstring explaining the purpose of the function
    """Function to check if a number is prime."""
    
    # Check if the number 'n' is less than or equal to 1, in which case it's not prime
    if n <= 1:
        # Immediately return False for numbers less than or equal to 1
        return False
    
    # Loop through numbers from 2 up to the square root of 'n' (inclusive) to check for factors
    for i in range(2, int(n**0.5) + 1):
        # Check if 'n' is divisible by the current number 'i'
        if n % i == 0:
            # If 'n' is divisible by 'i', it's not a prime number, so return False
            return False
    
    # If the loop completes without finding any factors, 'n' is prime, so return True
    return True

# Example usage: define a variable 'number' and assign it the value 23
number = 23
# Print whether the 'number' is prime by calling the 'is_prime' function with 'number' as the argument
print(f"{number} is prime: {is_prime(number)}")
'''


# First 10 primes 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.

''' 
Example:
If n = 25, then:

n**0.5 = 5.0

int(n**0.5) = 5

int(n**0.5) + 1 = 6

So, the loop will iterate over the numbers 2, 3, 4, 
and 5. Since 25 is divisible by 5, the loop will
find that 25 is not prime.
 '''