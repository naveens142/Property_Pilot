from app.rag import ask_question

while True:
    q = input("Ask your property question: ")
    if q.lower() == "exit":
        break
    print("\nAnswer:\n", ask_question(q))
