from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_docs(docs):
    if not docs:
        return []
    
    try:
        splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=100)  # Adjusted for better granularity
        chunks = splitter.split_documents(docs)
        return chunks
    
    except Exception as e:
        if __name__ == "__main__":
            print(f"Error splitting documents: {e}")
        return []
    
# Confirmation if run standalone
if __name__ == "__main__":
    from doc_load import load_docs
    documents = load_docs()
    chunks = split_docs(documents)
    print(f"Created {len(chunks)} chunks from {len(documents)} documents")   # No of chucnks from no of documents loaded
    if chunks and len(chunks) > 0:
        print(f"Sample chunk: {chunks[0].page_content[:100]}... (Metadata: {chunks[0].metadata})") # Sample chuncks and metadata
    if not chunks:
        print("Warning: No documents provided for splitting or no chunks created.")