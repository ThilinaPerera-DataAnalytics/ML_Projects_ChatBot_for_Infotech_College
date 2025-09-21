from pathlib import Path
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from doc_split import split_docs  # From doc_split.py

db_path =r"D:\Z1. Data Science Career\2. Python\Infotech\2025.08.29 - Project 3\ML_Projects_Infotech_College_ChatBot\chromadb"

def get_vectorstore(docs):
    try:
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2", model_kwargs={"device": "cpu"})
        if Path(db_path).exists() and any(Path(db_path).iterdir()):
            return Chroma(persist_directory=db_path, embedding_function=embeddings)
        chunks = split_docs(docs)
        vs = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory=db_path)
        return vs
    except Exception as e:
        print(f"Error in get_vectorstore: {e}")
        return None

# Confirmation if run standalone
if __name__ == "__main__":
    from doc_load import load_docs
    documents = load_docs(folder=r"D:\Z1. Data Science Career\2. Python\Infotech\2025.08.29 - Project 3\ML_Projects_Infotech_College_ChatBot\1_data")
    vectorstore = get_vectorstore(documents)
    if vectorstore and vectorstore._collection.count() > 0:
        print("Vector store loaded or created successfully!")
        print(f"Sample vector store count: {vectorstore._collection.count()} entries")
    elif vectorstore is None:
        print("Warning: Vector store creation failed.")
    else:
        print("Warning: No vectors created. Check document loading or chunking.")