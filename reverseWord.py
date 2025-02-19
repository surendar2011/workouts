# Reverse words in a sentence using a loop.

sentence = "Hello my dear team"

words = sentence.split()

reversed_words = []

for i in range (len(words) -1, -1, -1):
    reversed_words.append(words[i])

reversed_sentence = " ".join(reversed_words)

print(reversed_sentence)