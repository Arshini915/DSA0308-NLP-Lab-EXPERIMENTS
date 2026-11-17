from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Python is a programming language",
    "Machine learning uses Python",
    "Natural language processing is a part of AI",
    "Python is used for data science"
]

query = "Python programming"

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

query_vector = vectorizer.transform([query])

scores = cosine_similarity(query_vector, tfidf_matrix).flatten()

ranked_documents = scores.argsort()[::-1]

print("Information Retrieval System Using TF-IDF")
print("\nSearch Query:", query)

print("\nRanked Documents:")

for i in ranked_documents:
    print("Document:", documents[i])
    print("Relevance Score:", round(scores[i], 3))
    print()
