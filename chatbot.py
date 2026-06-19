import pandas as pd

# Load the FAQ dataset
faq = pd.read_csv("faq_dataset.csv")

print("=== FAQ Chatbot ===")
print("Type 'exit' to stop.\n")

while True:
    user_question = input("You: ")

    if user_question.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    found = False

    for index, row in faq.iterrows():
        if user_question.lower() == row["Question"].lower():
            print("Chatbot:", row["Answer"])
            found = True
            break

    if not found:
        print("Chatbot: Sorry, I don't know the answer to that question.")
        