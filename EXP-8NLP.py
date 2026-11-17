import nltk

from nltk.tag import UnigramTagger
from nltk.corpus import brown

nltk.download('brown')

train_data = brown.tagged_sents()[:500]

tagger = UnigramTagger(train_data)

sentence = "The cat is playing in the garden".split()

tags = tagger.tag(sentence)

print("Stochastic POS Tagging")
print("\nInput Sentence:")
print(" ".join(sentence))

print("\nPOS Tagged Output:")
for word, tag in tags:
    print(word, "->", tag)


#DONE BY:M.ARSHINI
    
