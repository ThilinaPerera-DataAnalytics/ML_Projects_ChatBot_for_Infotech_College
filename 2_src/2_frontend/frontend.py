import importlib
import os
import sys
import streamlit as st
from time import time

# ------------------------------
# Module imports
# ------------------------------
# Add chatbot source directory to module search path
script_dir = os.path.dirname(os.path.abspath(__file__))
chatbot_dir = os.path.join(script_dir, "..", "1_chatbot")  # Adjust relative path
chatbot_dir = os.path.abspath(chatbot_dir)
sys.path.append(chatbot_dir)

# Import custom modules
doc_load = importlib.import_module("doc_load")
doc_split = importlib.import_module("doc_split")
get_vectorstore = importlib.import_module("get_vectorstore")
clean = importlib.import_module("clean")
build_rag = importlib.import_module("build_rag")

# Assign functions
load_docs = doc_load.load_docs
split_docs = doc_split.split_docs
get_vectorstore = get_vectorstore.get_vectorstore
strip_think = clean.strip_think
build_rag = build_rag.build_rag

# ------------------------------
# Streamlit UI
# ------------------------------
st.set_page_config(page_title="Infotech College Digital Guide", layout="centered")
st.title("🏫 InfoTech College - Business/ IT 🎓\nVirtual Assistance Service")

# ------------------------------
# Initialize QA chain
# ------------------------------
if "qa_chain" not in st.session_state:
    with st.spinner("Initializing Digital Guide... This may take a moment..."):
        start_time = time()
        docs = load_docs(
            folder=r"D:\Z1. Data Science Career\2. Python\Infotech\2025.08.29 - Project 3\ML_Projects_Infotech_College_ChatBot\1_data"
        )
        if not docs:
            st.error("No documents found. Please add .txt, .md, or .pdf files to the `1_data` folder.")
        else:
            chunks = split_docs(docs)
            vs = get_vectorstore(chunks)
            if vs is None:
                st.error("Failed to create vector store. Check logs or dependencies.")
            else:
                st.session_state.qa_chain = build_rag(vs)
        st.success(f"Initialization complete in {time() - start_time:.2f} seconds.")

# ------------------------------
# User flow: Name → Chat
# ------------------------------
if "qa_chain" in st.session_state:
    if "user_name" not in st.session_state or not st.session_state.user_name:
        name_input = st.text_input("👤 Please enter your name to begin:")
        if name_input:
            st.session_state.user_name = name_input.strip()

    if "user_name" in st.session_state and st.session_state.user_name:
        st.write(
            f"🙋‍♀️ Hello **{st.session_state.user_name}**, welcome to Infotech College.\n\n"
            "I'm your Digital Guide, here to help you with any questions you have about "
            "courses, admissions, campus life, and more."
        )

        # Chat form
        with st.form(key="chat_form", clear_on_submit=True):
            user_input = st.text_input("🧐 What would you like to know? (type 'exit' to quit)")
            submit_button = st.form_submit_button(label="Send")

        # Handle chat interaction
        if submit_button and user_input:
            if user_input.lower() == "exit":
                st.success("✌️ Thank you for interacting with us. Have a great day.!")
            else:
                with st.spinner("Fetching your answer..."):
                    try:
                        start_time = time()
                        response = st.session_state.qa_chain.invoke(user_input)
                        end_time = time()
                        cleaned = (
                            strip_think(response["result"])
                            if "result" in response
                            else "No result returned."
                        )
                        st.markdown(f"**👩‍💻 Digital Guide:** {cleaned}")
                        st.caption(f"⏱ Response time: {end_time - start_time:.2f} seconds")
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
