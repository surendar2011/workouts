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

'''This code demonstrates several fundamental programming concepts in Python:
Loops: You learn how to use a for loop to iterate through a range of numbers (range(1500, 2701)). This is essential for processing sequences of data.
Conditional Statements: You learn how to use if statements to check conditions (x % 7 == 0 and x % 5 == 0). This allows you to execute specific code blocks only when certain criteria are met.

Modulo Operator: You use the modulo operator (%) to determine the remainder of a division. This is crucial for checking divisibility.

Data Structures: Lists: You learn how to create and manipulate lists (n1 = [], n1.append(str(x))). Lists are fundamental data structures for storing collections of items.

Data Type Conversion: You learn how to convert a number to a string using str(x). This is important when you need to work with numbers as text.

String Manipulation: You learn how to join elements of a list into a single string using the ','.join(n1) method. This is useful for formatting output.
In the Future, What Kinds of Code Can You Solve?
After understanding this code, you'll be able to tackle a variety of problems that involve:

Filtering Data:
Extracting specific items from a list based on certain criteria (e.g., finding all even numbers in a list, finding all words that start with a specific letter in a list of strings).
Identifying prime numbers within a given range.
Selecting data from a dataset that meets specific conditions.

Generating Sequences:
Creating lists of numbers that follow a specific pattern (e.g., the Fibonacci sequence, a sequence of squares).
Generating a series of dates or times.

Data Validation:
Checking if user input meets certain requirements (e.g., is a number within a valid range, is a string a valid email address).

Simple Data Analysis:
Calculating the sum, average, or other statistics of a set of numbers that meet specific criteria.
Counting the number of occurrences of a specific item in a list.'''