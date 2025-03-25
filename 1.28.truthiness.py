# Determine the truthiness of a value.

print(bool(0))        # Output: False
print(bool(1))        # Output: True
print(bool(""))       # Output: False (Empty string)
print(bool("hello"))  # Output: True (Non-empty string)
print(bool([]))       # Output: False (Empty list)
print(bool([1, 2]))   # Output: True (Non-empty list)
print(bool(None))     # Output: False (None is always False)
