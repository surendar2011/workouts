# first use def to get the value:

def sort_desc(lst):
    # use sorted mthd to sort and make it reverse
    return sorted(lst, reverse=True)


numbers = [5,2,9,1,7]
print(sort_desc(numbers))