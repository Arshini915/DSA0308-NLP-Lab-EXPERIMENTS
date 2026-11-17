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

sentence = "the boy eats a apple".split()

print("Parse Tree Generation Using CFG")
print("\nInput Sentence:")
print(" ".join(sentence))

print("\nParse Tree:")

trees = list(parser.parse(sentence))

if trees:
    for tree in trees:
        print(tree)
        tree.pretty_print()
else:
    print("No valid parse tree found.")
