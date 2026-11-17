import nltk
from nltk import RegexpParser
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')

text = "The intelligent student reads a book"

words = word_tokenize(text)
tags = pos_tag(words)

grammar = "NP: {<DT>?<JJ>*<NN.*>+}"

parser = RegexpParser(grammar)
tree = parser.parse(tags)

print("Syntax Driven Semantic Analysis")
print("\nInput Sentence:")
print(text)

print("\nNoun Phrases and Meanings:")

for subtree in tree.subtrees():
    if subtree.label() == 'NP':
        phrase = " ".join(word for word, tag in subtree.leaves())
        print("\nNoun Phrase:", phrase)

        for word, tag in subtree.leaves():
            if tag.startswith('NN'):
                synsets = wordnet.synsets(word, pos=wordnet.NOUN)
                if synsets:
                    print(word, ":", synsets[0].definition())
