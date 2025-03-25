# Find the frequency of each character in a string. Collections - counters

# you are importing Counter from the collections module.
# We import Counter from collections because it is a built-in tool for counting elements.
from collections import Counter

def character_frequency(s):
    return Counter(s)

# Example usage:
s = "hello world"
freq = character_frequency(s)
print(freq)



from collections import Counter

s = "hello world"
freq = Counter(s)  # Directly using Counter without a function
print(freq)


# Output:
# Counter({'l': 3, 'o': 2, ' ': 1, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1})