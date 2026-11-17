import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('omw-1.4')

word = "computer"

synsets = wordnet.synsets(word)

print("WordNet - Word Meaning")

print("\nInput Word:", word)

print("\nSynsets and Meanings:")

for syn in synsets:
    print("\nSynset:", syn.name())
    print("Meaning:", syn.definition())
    print("Examples:", syn.examples())

print("\nSynonyms:")

for syn in synsets:
    for lemma in syn.lemmas():
        print(lemma.name())
