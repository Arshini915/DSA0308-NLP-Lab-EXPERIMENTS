import re

def recognize_dialog_act(sentence):
    sentence = sentence.lower().strip()

    if re.search(r'\b(hi|hello|hey|good morning|good evening)\b', sentence):
        return "Greeting"

    elif sentence.endswith("?"):
        return "Question"

    elif re.search(r'\b(please|kindly|could you|can you)\b', sentence):
        return "Request"

    elif re.search(r'\b(thank you|thanks)\b', sentence):
        return "Thanking"

    elif re.search(r'\b(bye|goodbye|see you)\b', sentence):
        return "Goodbye"

    else:
        return "Statement"

dialog = [
    "Hello, how are you?",
    "What is your name?",
    "Please help me",
    "Thank you",
    "I am a student",
    "Goodbye"
]

print("Dialog Act Recognition")

for sentence in dialog:
    act = recognize_dialog_act(sentence)
    print("\nSentence:", sentence)
    print("Dialog Act:", act)

#done by M.ARSHINI(192424322)
