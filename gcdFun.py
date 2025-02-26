# def gcd(a, b):
    
#     while b:
#         a, b = b, a % b
#     return abs(a)

# # Example usage:
# print(gcd(48, 18))  # Output: 6

''' 
Function Definition: The gcd(a, b) function takes two integers as input and returns their GCD.

Euclidean Algorithm: The algorithm works by repeatedly replacing a with b and b with the remainder of a divided by b, until b becomes zero. 
At that point, a is the GCD.

Absolute Value: The function returns the absolute value of a to ensure the result is always positive, even if the inputs are negative.

Example Usage: The example shows how to use the function to find the GCD of 48 and 18, which is 6.

 '''


# first use the def to get two values:
def gcd(a,b):

    # run the loop until b become 0.
    while b:
        # continuously swapping a to b, b with a reminder of b until zero, b becomes zero focus on a is the gcd value
        a,b = b, a % b
    return abs(a)

print(gcd(48,18))