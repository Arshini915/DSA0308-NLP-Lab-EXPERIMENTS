
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = """Python is a programming language.
Python is used for machine learning.
Machine learning is a part of artificial intelligence.
Artificial intelligence is used in many applications."""

sentences = sent_tokenize(text)

vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(sentences)

similarity = cosine_similarity(tfidf)

scores = []

print("Text Coherence Evaluation")
print("\nInput Text:")
print(text)

print("\nSentence Similarity:")

for i in range(len(sentences) - 1):
    score = similarity[i][i + 1]
    scores.append(score)
    print("Sentence", i + 1, "and", i + 2, ":", round(score, 2))

if scores:
    average = sum(scores) / len(scores)
else:
    average = 0

print("\nCoherence Score:", round(average, 2))

if average >= 0.3:
    print("Text is Coherent")
else:
    print("Text has Low Coherence")
