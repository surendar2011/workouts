# Sort a list in ascending order without using sort().

# Bubble sort works by repeatedly swapping the adjacent elements if they are in the wrong order.
# Selection sort works by selecting the smallest element from the unsorted part of the list and swapping it with the first unsorted element.
# Insertion sort works by iterating through the list one element at a time, inserting each element into its proper position in the sorted part of the list.

# *Insertion Sort also has a time complexity of O(n²) but performs better on nearly sorted lists.


my_list = [64, 34, 25, 12, 22, 11, 90]

my_list = [34, 64, 25, 12, 22, 11, 90]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = insertion_sort(my_list)
print("Sorted List:", sorted_list)

# Good question!

# After exiting the while loop, j is -1.

# Now, arr[j + 1] = key means arr[-1 + 1] = key, which simplifies to arr[0] = key.

# That’s why key (25) is placed at arr[0]. 