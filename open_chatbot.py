import importlib
import os
import sys

# Add the 2_src/1_chatbot directory to the module search path
script_dir = os.path.dirname(os.path.abspath(__file__))
chatbot_dir = os.path.join(script_dir, "2_src", "1_chatbot")
sys.path.append(chatbot_dir)

# Import modules directly using their names
doc_load = importlib.import_module('doc_load')
doc_split = importlib.import_module('doc_split')
get_vectorstore = importlib.import_module('get_vectorstore')
build_rag = importlib.import_module('build_rag')
chat_interactive = importlib.import_module('chat_interactive')

# Then use the functions
load_docs = doc_load.load_docs
split_docs = doc_split.split_docs
get_vectorstore = get_vectorstore.get_vectorstore
build_rag = build_rag.build_rag
chat_interactive = chat_interactive.chat_interactive

if __name__ == "__main__":
    docs = load_docs(folder=r"D:\Z1. Data Science Career\2. Python\Infotech\2025.08.29 - Project 3\ML_Projects_Infotech_College_ChatBot\1_data")
    if not docs:
        raise ValueError("No documents found in '.\1_data'. Please add .txt, .md, or .pdf files.")
    docs = split_docs(docs)
    vs = get_vectorstore(docs)
    rag_chain = build_rag(vs)
    chat_interactive(rag_chain)  # Pass the RAG chain