import nltk

from nltk.tokenize import word_tokenize

text = "Ravi is a student. He studies Python. Ravi likes programming."

words = word_tokenize(text)

nouns = ["Ravi", "student", "Python", "programming"]

pronouns = {
    "He": "Ravi",
    "She": "Priya",
    "It": "Python",
    "They": "Students"
}

print("Reference Resolution")
print("\nInput Text:")
print(text)

print("\nResolved References:")

for word in words:
    if word in pronouns:
        print(word, "->", pronouns[word])
