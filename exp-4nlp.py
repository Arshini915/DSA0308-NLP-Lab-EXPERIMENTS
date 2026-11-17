def pluralize(word):
    if word.endswith(("s", "sh", "ch", "x", "z")):
        return word + "es"
    elif word.endswith("y") and word[-2] not in "aeiou":
        return word[:-1] + "ies"
    else:
        return word + "s"

words = ["cat", "box", "baby", "bus", "dish"]

print("Finite State Machine - Plural Formation")

for word in words:
    plural = pluralize(word)
    print(word, "->", plural)
