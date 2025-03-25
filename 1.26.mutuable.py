# Check if a variable is mutable.

#What Happens If We Remove It?
# If you don’t compare the memory addresses, you might assume an object is mutable just because Python didn’t throw an error.
# But some objects (like tuples or strings) simply cannot be modified in place. Without checking the ID, you won’t know for sure. 

# id() returns memory address
# isinstance() returns true or false, is giving type is same or not.

def is_mutable(variable):
    initial_id = id(variable)  # Get the initial memory address

    try:
        # Attempt to modify the variable
        if isinstance(variable, list):
            variable.append(1)
        elif isinstance(variable, dict):
            variable["test"] = 1
        elif isinstance(variable, set):
            variable.add(1)
        elif isinstance(variable, bytearray):
            variable.append(1)
        else:
            return False  # If modification is not possible, it's immutable

        # Check if the memory address remains the same
        return id(variable) == initial_id

    except (TypeError, AttributeError):
        return False  # If an error occurs, it's immutable

# **Example Usage**
print(is_mutable([1, 2, 3]))  # Output: True (Lists are mutable)
print(is_mutable((1, 2, 3)))  # Output: False (Tuples are immutable)
print(is_mutable({1, 2, 3}))  # Output: True (Sets are mutable)
print(is_mutable(42))         # Output: False (Integers are immutable)
print(is_mutable("hello"))    # Output: False (Strings are immutable)
print(is_mutable(bytearray(b"abc")))  # Output: True (Bytearrays are mutable)
