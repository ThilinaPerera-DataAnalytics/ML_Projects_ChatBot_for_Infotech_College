import glob
from pathlib import Path
from langchain_community.document_loaders import TextLoader, PyPDFLoader

def load_docs(folder=r"D:\Z1. Data Science Career\2. Python\Infotech\2025.08.29 - Project 3\ML_Projects_Infotech_College_ChatBot\1_data"): 
    docs = []  # Creates an empty list which will hold all loaded documents.

    try:
        for ext in ("*.txt", "*.md"):
            for file in glob.glob(str(Path(folder) / "**" / ext), recursive=True):  # Search all subfolders for .txt and .md files
                docs.extend(TextLoader(file).load())  # Load .txt/.md document and add to the list
        for file in glob.glob(str(Path(folder) / "**" / "*.pdf"), recursive=True):  # Search all subfolders for .pdf files
            docs.extend(PyPDFLoader(file).load())  # Load .pdf document and add to the list
        return docs
    
    except Exception as e:
        if __name__ == "__main__":
            print(f"Error processing folder {folder}: {e}")
        return []

# Confirmation if run standalone
if __name__ == "__main__":
    documents = load_docs()
    if documents and len(documents) > 0:
        print(f"Loaded {len(documents)} documents from {'./1_data'}")  # No of documents loaded
    if not documents:
        print("Warning: No documents were loaded. Check folder path or file formats.")
