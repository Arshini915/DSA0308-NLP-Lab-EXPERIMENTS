import re

text = input("enter your sentence: ")

text = re.sub("Chennai", "Bangalore", text)
text = re.sub(r"booking ID \d+", "booking ID 192424322", text)

print("Replaced Sentence:", text)

#done by M.Arshini(192424322)
