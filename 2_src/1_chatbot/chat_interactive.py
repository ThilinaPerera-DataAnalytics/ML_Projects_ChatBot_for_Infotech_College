from clean import strip_think
from build_rag import build_rag

def chat_interactive(qa_chain):
    print("\nHello, \nWelcome to Infotech College. I'm your digital guide, here to help you with any questions you have about courses, admissions, campus life, and more. What would you like to know? (type 'exit' to quit).\n")
    while True:
        query = input("You: ").strip()
        if query.lower() == "exit":
            print("\nThank you for the interest. Have a great day.!")
            break
        try:
            answer = qa_chain.invoke(query)
            cleaned = strip_think(answer['result'])
            print(f"\nDigital Guide: {cleaned}\n")
        except Exception as e:
            print(f"Error processing your question: {e}\n")

# Confirmation if run standalone
if __name__ == "__main__":
    import time
    from doc_load import load_docs
    from doc_split import split_docs
    from get_vectorstore import get_vectorstore
    documents = load_docs(folder=r"D:\Z1. Data Science Career\2. Python\Infotech\2025.08.29 - Project 3\ML_Projects_Infotech_College_ChatBot\1_data")
    chunks = split_docs(documents)
    vectorstore = get_vectorstore(chunks)
    qa_chain = build_rag(vectorstore)
    print("\nStarting the interactive test session...")

    your_name = input("\nType your name: ")
    
    print(f"\nHello {your_name}, \nWelcome to Infotech College. I'm your Digital Guide, here to help you with any questions you have about courses, admissions, campus life, and more. What would you like to know? (type 'exit' to quit).")
    while True:
        query = input(f"{your_name}: ").strip()
        if query.lower() == "exit":
            print("\nThank you for the interest. Have a great day.!")
            break
        try:
            start_time = time.time()
            answer = qa_chain.invoke(query)
            cleaned_answer = strip_think(answer['result'])
            end_time = time.time()
            print(f"Digital Guide: {cleaned_answer}")
            print(f"\nResponse time: {end_time - start_time:.2f} seconds\n")
        except Exception as e:
            print(f"Error processing your question: {e}\n")