import nltk

grammar = nltk.CFG.fromstring("""
S -> NP_SG VP_SG
S -> NP_PL VP_PL
NP_SG -> Det_SG N_SG
NP_PL -> Det_PL N_PL
VP_SG -> V_SG
VP_PL -> V_PL
Det_SG -> 'the' | 'a'
Det_PL -> 'the'
N_SG -> 'boy' | 'girl'
N_PL -> 'boys' | 'girls'
V_SG -> 'runs' | 'plays'
V_PL -> 'run' | 'play'
""")

parser = nltk.ChartParser(grammar)

sentences = [
    "the boy runs",
    "the girls play",
    "the boy play",
    "the girls runs"
]

for sentence in sentences:
    words = sentence.split()
    trees = list(parser.parse(words))

    print("\nSentence:", sentence)

    if trees:
        print("Result: Correct Agreement")
    else:
        print("Result: Incorrect Agreement")


#DONE BY:M.ARSHINI(192424322)
