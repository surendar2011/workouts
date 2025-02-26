# Create a function to filter out negative numbers from a list.

def filter_negatives(lst):
    return [x for x in lst if x >= 0]  # Keep only non-negative numbers

numbers = [-5, 3, -1, 7, 0, -8, 10]

print(filter_negatives(numbers))  # Output: [3, 7, 0, 10]


'''
✅ Yes, x is being added (appended) to a new 
list automatically, without calling .append().

'''