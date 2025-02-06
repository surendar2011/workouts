# Prompt the user to input a temperature in the format (e.g., 45F, 102C, etc.)
temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")

# Extract the numerical part of the temperature and convert it to an integer
try:
    degree = int(temp[:-1])
except ValueError:
    print("Invalid input: Please enter a number followed by 'C' or 'F'.")
    quit()

# Extract the convention part of the temperature input (either 'C' or 'F')
i_convention = temp[-1]

# Check if the input convention is in uppercase 'C' (Celsius)
if i_convention.upper() == "C":
    # Convert the Celsius temperature to Fahrenheit
    result = int(round((9 * degree) / 5 + 32))
    o_convention = "Fahrenheit"  # Set the output convention as Fahrenheit

# Check if the input convention is in uppercase 'F' (Fahrenheit)
elif i_convention.upper() == "F":
    # Convert the Fahrenheit temperature to Celsius
    result = int(round((degree - 32) * 5 / 9))
    o_convention = "Celsius"  # Set the output convention as Celsius

else:
    # If the input convention is neither 'C' nor 'F', print an error message and exit the program
    print("Input proper convention.")
    quit()

# Display the converted temperature in the specified output convention
print("The temperature in", o_convention, "is", result, "degrees.")

'''What You Will Learn

1.  User Input and Data Handling:
    *   `input()` function: You'll learn how to prompt the user to enter data and store it in a variable (`temp`).
    *   String slicing:  You'll practice extracting specific parts of a string using slicing (`temp[:-1]` to get the numerical part and `temp[-1]` to get the convention).
    *   Data type conversion: You'll convert the numerical part of the input string to an integer using `int()`. This is crucial for performing calculations.
    *   Error handling (try-except):  You'll use a `try-except` block to handle potential `ValueError` exceptions that can occur if the user enters non-numeric input. This makes your program more robust.

2.  Conditional Logic:
    *   `if-elif-else` statements: You'll use these statements to control the flow of the program based on the input convention ('C' or 'F').  This is fundamental for decision-making in programming.
    *   String comparison: You'll compare strings using `i_convention.upper() == "C"` to check the input convention (case-insensitively).

3.  Mathematical Operations:
    *   You'll apply the formulas for converting between Celsius and Fahrenheit.
    *   You'll use `round()` to round the result to the nearest integer.

4.  Output:
    *   `print()` function: You'll display the converted temperature along with the output convention.

How This Will Be Helpful in the Future

1.  Problem Solving:  This script demonstrates a simple problem-solving approach:
    *   Breaking down a problem:  The task of temperature conversion is broken down into smaller, manageable steps (input, processing, output).
    *   Algorithm design:  The script follows a clear algorithm to perform the conversion based on the input.

2.  Foundation for More Complex Programs: The concepts you learn in this script are building blocks for more complex programs. You'll use these skills in many different contexts:
    *   Data validation:  The error handling in this script is a basic form of data validation, which is essential for ensuring the correctness of your programs.
    *   User interfaces: When you create programs with graphical user interfaces (GUIs), you'll use similar techniques to get input from the user and display output.
    *   Data processing:  Many programs involve processing data based on certain conditions, and the `if-elif-else` statements will be crucial for that.

3.  Practical Applications:
    *   You can adapt this script to convert between other units of measurement (e.g., kilometers to miles, kilograms to pounds).
    *   You can integrate this script into larger applications that require temperature conversions, such as weather forecasting tools or scientific simulations.

4.  Thinking Like a Programmer: By working through this script, you'll start to develop the mindset of a programmer:
    *   Attention to detail:  You'll learn to pay attention to small details, such as data types, string slicing, and error handling.
    *   Logical thinking: You'll learn to think logically and break down problems into smaller, more manageable steps.
    *   Testing and debugging: You'll learn to test your code and fix any errors that arise.

In summary, this simple temperature conversion script provides a solid foundation in basic programming concepts that will be valuable for tackling more complex problems in the future.'''
