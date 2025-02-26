# Count the number of vowels in a string.

vowels = "aeiouAEIOU"
word = "surendar"

count = 0

for c in word:
    if c in vowels:
        count += 1

print(count)