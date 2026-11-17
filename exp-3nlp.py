import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('omw-1.4')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = ["playing", "played", "studies", "running", "happiness"]

print("Morphological Analysis Using NLTK")

for word in words:
    print("\nOriginal Word:", word)
    print("Stemming:", stemmer.stem(word))
    print("Lemmatization:", lemmatizer.lemmatize(word, pos='v'))



#done by M.ARSHINI(192424322)
