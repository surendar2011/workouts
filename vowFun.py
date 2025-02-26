# Create a function to count the number of vowels in a string.


def count_vowels(word):

    vowels = "aeiouAEIOU"
    count = 0

    for char in word:
        if char in vowels:
            count += 1

    return count

word = "surendar"
print(count_vowels(word))