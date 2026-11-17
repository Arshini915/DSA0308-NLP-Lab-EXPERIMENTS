import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'boy' | 'girl' | 'dog' | 'apple'
V -> 'eats' | 'sees'
""")

parser = nltk.ChartParser(grammar)

sentence = "the boy eats an apple".replace("an apple", "a apple").split()

print("Top-Down Parsing Using CFG")
print("\nInput Sentence:")
print(" ".join(sentence))

print("\nParsing Tree:")

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
