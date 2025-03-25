# Remove duplicates from a list using loops.

# Original list with duplicates
my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

# Initialize an empty list to store unique elements
unique_list = []

# Loop through each element in the original list
for item in my_list:
    if item not in unique_list:  # Check if the item is not already in unique_list
        unique_list.append(item)  # Add the item to unique_list if it's not a duplicate

# Print the list without duplicates
print("List without duplicates:", unique_list)


# Using set() Example:

# # Original list with duplicates
# my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

# # Convert the list to a set to remove duplicates
# unique_list = list(set(my_list))

# # Print the list without duplicates
# print("List without duplicates:", unique_list)