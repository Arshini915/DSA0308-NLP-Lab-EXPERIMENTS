import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

text = "The students are learning Python programming"

words = nltk.word_tokenize(text)

tags = nltk.pos_tag(words)

print("Part-of-Speech Tagging")
print("\nInput Text:")
print(text)

print("\nPOS Tagged Output:")

for word, tag in tags:
    print(word, "->", tag)

#DONE BY:M.ARSHINI
