import spacy

nlp = spacy.load("en_core_web_sm")

text = "Apple was founded by Steve Jobs in California in 1976."

doc = nlp(text)

print("Named Entity Recognition Using SpaCy")
print("\nInput Text:")
print(text)

print("\nNamed Entities:")

for ent in doc.ents:
    print(ent.text, "->", ent.label_)
