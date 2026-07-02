from transformers import pipeline

# parse input
inp = input()  

ans = pipeline("question-answering")
summarizer = pipeline("summarization")

context = input("Enter the doc for context: ")
print("Here is a quick summmary: ", summarizer(context, max_length=len(context)//3))

while (True):
    question = input("Ask a question about the doc (q to quit): ")
    if question == "q": break
    raw_output = ans (
            question=question,
            context=context
            )
    print(raw_output['answer'])
