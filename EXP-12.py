import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'boy' | 'girl' | 'dog' | 'apple'
V -> 'eats' | 'sees'
""")

parser = nltk.EarleyChartParser(grammar)

sentence = "the boy eats a apple".split()

print("Earley Parser Using NLTK")
print("\nInput Sentence:")
print(" ".join(sentence))

print("\nParsing Tree:")

trees = list(parser.parse(sentence))

if trees:
    for tree in trees:
        print(tree)
        tree.pretty_print()
else:
    print("Sentence is not accepted by the grammar.")
