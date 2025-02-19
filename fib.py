# def fibonacci_for_loop(n):
#     """
#     Generate the first n Fibonacci numbers using a for loop.
#     """
#     fib_list = []
#     a, b = 0, 1
#     # used _ empty holder don't actually need the value of the loop counter
#     for _ in range(n):
#         fib_list.append(a)
#         a, b = b, a + b
#     return fib_list

# # Example usage:
# num_terms = 10
# fibonacci_sequence = fibonacci_for_loop(num_terms)
# print(f"Fibonacci sequence up to {num_terms} terms: {fibonacci_sequence}")

# use a def function for loop
def fibonacci_for_loop(n):
    # use a empty list
    fib_list = []
    # initialize first two values
    a, b = 0, 1
    # use a for loop for the range
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list

num_terms = 10
fibonacci_sequence = fibonacci_for_loop(num_terms)
print(f"Fib seq up to {num_terms} terms: {fibonacci_sequence}")
