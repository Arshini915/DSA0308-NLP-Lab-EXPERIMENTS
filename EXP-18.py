import re

def parse(expression):
    expression = expression.strip()

    patterns = [
        (r'^forall\s+\w+\s*:\s*.+$', "Universal Quantifier"),
        (r'^exists\s+\w+\s*:\s*.+$', "Existential Quantifier"),
        (r'^[A-Za-z]\w*\([^()]*\)$', "Predicate"),
        (r'^.+\s+AND\s+.+$', "Logical AND"),
        (r'^.+\s+OR\s+.+$', "Logical OR"),
        (r'^NOT\s+.+$', "Logical NOT"),
        (r'^.+\s+IMPLIES\s+.+$', "Implication")
    ]

    for pattern, meaning in patterns:
        if re.match(pattern, expression):
            return meaning

    return "Invalid Expression"

expressions = [
    "forall x: Human(x)",
    "exists y: Student(y)",
    "Loves(John, Mary)",
    "Human(x) AND Mortal(x)",
    "Student(x) OR Teacher(x)",
    "NOT Happy(x)",
    "Rain(x) IMPLIES Wet(x)"
]

print("FOPC Parser")

for exp in expressions:
    print(exp, "->", parse(exp))
