# Check if a string contains only digits. isdigit()
# use the .isdigit() method in Python to check if a string contains only digits.

s = "12345"
print(s.isdigit())  # Output: True

s = "123a5"
print(s.isdigit())  # Output: False

s = " 12345 "
print(s.isdigit())  # Output: False (because of spaces)

s = " 12345 "
print(s.strip().isdigit())  # Output: True