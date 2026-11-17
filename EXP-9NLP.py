import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

nltk.download('punkt')
nltk.download('punkt_tab')

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*ly$', 'RB'),
    (r'.*ous$', 'JJ'),
    (r'.*', 'NN')
]

tagger = RegexpTagger(patterns)

text = "The students are learning Python quickly"

words = word_tokenize(text)

tags = tagger.tag(words)

print("Rule-Based POS Tagging")
print("\nInput Text:")
print(text)

print("\nPOS Tagged Output:")

for word, tag in tags:
    print(word, "->", tag)


#DONE BY:M.ARSHINI(192424322)
