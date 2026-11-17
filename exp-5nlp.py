from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["playing", "played", "plays", "running", "runner", "studies", "happiness"]

print("Word Stemming Using Porter Stemmer")

for word in words:
    print(word, "->", stemmer.stem(word))


#M.ATRSHINI(192424322)
