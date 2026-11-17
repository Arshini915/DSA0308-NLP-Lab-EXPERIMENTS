import nltk
from nltk.tag import RegexpTagger, BrillTaggerTrainer
from nltk.tag.brill import Template
from nltk.tag.brill_trainer import BrillTaggerTrainer

nltk.download('brown')

from nltk.corpus import brown

train_data = brown.tagged_sents(categories='news')[:500]

initial_tagger = RegexpTagger([
    (r'.*ing$', 'NN'),
    (r'.*ed$', 'VB'),
    (r'.*ly$', 'JJ'),
    (r'.*', 'NN')
])

templates = [
    Template(nltk.tag.brill.Pos([-1])),
    Template(nltk.tag.brill.Word([-1]))
]

trainer = BrillTaggerTrainer(initial_tagger, templates, trace=0)

tagger = trainer.train(train_data, max_rules=10)

sentence = "The students are learning Python quickly".split()

print("Transformation Based POS Tagging")
print("\nInput Sentence:")
print(" ".join(sentence))

print("\nPOS Tagged Output:")

for word, tag in tagger.tag(sentence):
    print(word, "->", tag)
