from ollama import Client
from get_vectorstore import get_vectorstore
from doc_load import load_docs

ollama_client = Client(host='http://localhost:11434') # Initialize Ollama client

def get_llm_response(query):
    # Load documents and get vector store
    documents = load_docs(folder=r"D:\Z1. Data Science Career\2. Python\Infotech\2025.08.29 - Project 3\ML_Projects_Infotech_College_ChatBot\1_data")
    vectorstore = get_vectorstore(documents)
    
    # Retrieve relevant documents
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})  # Top 5 similar chunks
    retrieved_docs = retriever.invoke(query)
    
    # Combine query with retrieved context
    context = "\n".join([doc.page_content for doc in retrieved_docs])
    prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
    
    # Generate response using DeepSeek via Ollama
    response = ollama_client.chat(
        model="deepseek-r1:1.5b",  # Matches loaded model
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response['message']['content']

# Confirmation if run standalone
if __name__ == "__main__":
    import time
    test_query = "What courses does InfoTech College offer?"
    start_time = time.time()
    answer = get_llm_response(test_query)
    end_time = time.time()
    print(f"Question: {test_query}")
    print(f"Answer: {answer}")
    print(f"Response time: {end_time - start_time:.2f} seconds")