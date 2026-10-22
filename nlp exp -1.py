import re

text = input("Enter your sentence: ")

text = re.sub("Chennai", "Bangalore", text)
text = re.sub(r"booking ID \d+", "booking ID 192424322", text)

print("Replaced Sentence:", text)
