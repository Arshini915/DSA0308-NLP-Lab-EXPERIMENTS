import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('omw-1.4')

sentence = "I went to the bank to deposit money"

words = word_tokenize(sentence)

result = lesk(words, 'bank')

print("Word Sense Disambiguation Using Lesk Algorithm")
print("\nInput Sentence:")
print(sentence)

print("\nAmbiguous Word: bank")

if result:
    print("Meaning:", result.definition())
    print("Synset:", result.name())
else:
    print("No meaning found")

#DONE BY:M.ARSHINI(192424322)
