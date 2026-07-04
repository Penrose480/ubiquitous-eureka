from transformers import pipeline

# parse input
inp = input()  

ans = pipeline("question-answering", model="deepset/roberta-base-squad2")

context = input("Enter the doc for context: ")

while (True):
    question = input("Ask a question about the doc (q to quit): ")
    if question == "q": break
    raw_output = ans (
            question=question,
            context=context
            )
    print(raw_output['answer'])
