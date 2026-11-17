import random

text = "I love machine learning. I love Python programming. Python is easy to learn."

words = text.lower().replace(".", "").split()

bigrams = {}

for i in range(len(words) - 1):
    current = words[i]
    next_word = words[i + 1]

    if current not in bigrams:
        bigrams[current] = []

    bigrams[current].append(next_word)

word = "i"
result = [word]

for i in range(10):
    if word in bigrams:
        word = random.choice(bigrams[word])
        result.append(word)
    else:
        break

print("Generated Text:")
print(" ".join(result))

#DONE BY:M.ARSHINI(192424322)
