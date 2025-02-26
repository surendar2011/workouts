# Write a function to check if a string is a palindrome.
# Create a function to swap two variables.

'''
def panlin(word):
    if word == word[::-1]:  # Check if the word is the same when reversed
        print("Yes")
    else:
        print("No")

word = 'tenet'
panlin(word)  # Output: Yes
'''


def swapped(a,b):

    a,b = b,a
    return a,b

a = 5
b = 1

print(*swapped(a,b))

# The * operator unpacks the tuple into separate values.