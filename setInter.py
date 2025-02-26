# Create a function that returns the intersection of two sets.

def intersection (set1, set2):
    return set1 & set2 # Using '&' operator for set intersection

set_a = {1,2,3,4}
set_b = {3,4,5,6}

print(intersection(set_a, set_b))


# & is the set intersection operator, which finds common elements in both sets.
