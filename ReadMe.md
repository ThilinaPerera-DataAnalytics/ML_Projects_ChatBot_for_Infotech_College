# 🤖 Developing a ChatBot for InfoTech College of Business and IT


```
Individual Project 03
Machine Learning with Advanced Python
Infotech College of Business & IT
```
![alt text](cover_image.png)

A Retrieval-Augmented Generation (RAG) powered chatbot built for Infotech College
, enabling students and visitors to ask questions about courses, admissions, campus life, and more.

This project showcases practical use of **Large Language Models (LLMs)**, **Vector Databases**, and **Retrieval-Augmented Generation** to build a domain-specific assistant.

[![Demo Video](https://img.shields.io/badge/Demo-Video-blue)](https://drive.google.com/file/d/1cu-lLNyw4Zzq5NdTNp3v4W_iPnXPAHrT/view?usp=sharing)
[![Dataset](https://img.shields.io/badge/Dataset-GoogleDrive-orange)](https://drive.google.com/drive/folders/13zkRvYOpuv95XYIMl-vMVmHzPCEppjqF?usp=sharing)

---
## 📌 Features

* ✅ **Document Processing**: Loads and splits college PDFs into retrievable knowledge chunks
* ✅ **Vector Search**: Embeddings stored in **ChromaDB** for fast retrieval
* ✅ **LLM Integration**: Powered by **Ollama** with **DeepSeek-r1 (1.5B)** model
* ✅ **RAG Pipeline**: Retrieval + Prompting + Context-aware responses
* ✅ **Interactive CLI**: Ask questions directly from terminal
* ✅ **Streamlit UI**: Simple front-end interface for users
* ✅ **Clean Responses**: Custom function strips unnecessary “thinking” text from LLM outputs

---
## 📂 Project Structure

```
ML_Projects_ChatBot_for_Infotech_College/
│── 1_data/                  # PDF documents (college info, about us, admissions, etc.)
|
│── 2_src/
│   ├── 1_chatbot/
│   │   ├── doc_load.py       # Load PDFs
│   │   ├── doc_split.py      # Split into chunks
│   │   ├── get_vectorstore.py # Create & save embeddings
│   │   ├── integrate_llm.py   # Connect to Ollama LLM
│   │   ├── build_rag.py       # RAG pipeline
│   │   ├── clean.py           # Strip unwanted LLM text
│   │   ├── chat_interactive.py # CLI chatbot
│   │   └── open_chatbot.py     # Final chatbot entrypoint
│   └── 2_frontend/
│      └── frontend.py        # Streamlit interface (optional)
│
│── .git/
│── chromadb/
│
│── requirements.txt
│── README.md
└── cover_image.png
```

## 🛠️ Tech Stack

* **Python 3.11**
* **LangChain** (RAG pipeline & integrations)
* **ChromaDB** (vector database)
* **Ollama** (local LLMs: DeepSeek-r1)
* **HuggingFace Sentence Transformers** (`all-MiniLM-L6-v2` for embeddings)
* **Streamlit** (UI)

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/ThilinaPerera-DataAnalytics/ML_Projects_ChatBot_for_Infotech_College.git
cd ML_Projects_ChatBot_for_Infotech_College
```

### 2. Create environment

```bash
conda create -n infochatbot python=3.11
conda activate infochatbot
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup Ollama & models

Install Ollama → [ollama.com](https://ollama.com/)

```bash
ollama pull deepseek-r1:1.5b
```

### 5. Run pipeline scripts

```bash
# Load documents
python 2_src/1_chatbot/doc_load.py

# Split into chunks
python 2_src/1_chatbot/doc_split.py

# Create vectorstore
python 2_src/1_chatbot/get_vectorstore.py

# Run chatbot interactively
python 2_src/1_chatbot/chat_interactive.py
```

### 6. Run Streamlit UI

```bash
streamlit run 2_src/2_frontend/frontend.py
```

Then open: [http://localhost:8501](http://localhost:8501)

---

## 💡 Example Queries

**Q:** *How can I enroll at Infotech College?*
**A:** Visit [Enrollment Page](https://www.infotechcollege.com/enrollment/). Payment options include monthly installments, full payment, or smaller installment fees.

**Q:** *What courses are offered?*
**A:** Foundation in Information Technology (FIT) program, recognized by the University of Colombo School of Computing (UCSC), plus other IT-focused offerings.

**Q:** *Can I study medicine there?*
**A:** Infotech College specializes in IT & AI programs, not medicine.

---

## 📊 Performance

* **Mistral (7.3B)** → \~200 sec response time (on Lenovo T530)
* **DeepSeek-r1 (1.5B)** → \~60 sec response time (chosen for final chatbot)
* **Vector store size** → 63 embeddings across 39 documents

---

## 🎯 Key Learnings

* Practical application of **RAG pipelines** for domain-specific QA
* Trade-offs between **different LLM sizes** (speed vs detail)
* Building both **CLI** and **Web-based** chatbot interfaces

---

## 📌 Next Steps




## 🤝 Contributing

Contributions are welcome! Please fork the repo and submit a pull request with improvements.


## 👨‍💻 Author

**Thilina Perera**

    📌 Data Analytics Enthusiast | Machine Learning, Deep Learning, LLM/ LMM & NLP Explorer

🔗 [LinkedIn](https://www.linkedin.com/in/thilina-perera-148aa934/) | [GitHub](https://github.com/ThilinaPerera-DataAnalytics)

---

## ⭐ Acknowledgement
    *



✨ If you like this project, don’t forget to **star ⭐ the repo**!




