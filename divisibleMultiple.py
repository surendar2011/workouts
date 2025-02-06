# Write a Python program to find those numbers which are divisible 
# by 7 and multiples of 5, between 1500 and 2700 (both included).

# create an empty list to store numbers that meet the given conditions:
n1 = []

# Iterate through numbers from 1500 to 2700
for x in range(1500, 2701):
    #check if the number is divisible by 7 and 5 without remainder
    if (x % 7 == 0) and (x % 5 == 0):
        #if the conditions are met, convert the number to string and 
        # append to the list
        n1.append(str(x))

# join the numbers in the list with a comma and print the result.
print(','.join(n1))
