# Write a function that takes a list and returns a new list with squared values.


def num_lis(n):
    # Squaring each number in the list
    return [i ** 2 for i in n]  

n = [1, 2, 3]

print(num_lis(n))  # Output: [1, 4, 9]

'''
✅ Yes, i is being added (appended) to a new 
list automatically, without calling .append().

'''