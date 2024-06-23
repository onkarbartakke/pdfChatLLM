import streamlit as st
from dotenv import load_dotenv
import pickle
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
import os


with st.sidebar:
    st.title('🤗💬 LLM Chat App')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model
 
    ''')
    add_vertical_space(5)
    st.write('Made with ❤️ by [Onkar Bartakke](https://www.linkedin.com/in/onkar-bartakke-9a45411a5/)')
 

def main():
    st.header("Chat with PDF 💬: ")

    #upload a pdf file
    pdf = st.file_uploader("Upload your PDF", type='pdf')
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        st.write(pdf_reader)

        text= ""

        for page in pdf_reader.pages:
            text += page.extract_text()
        
        st.write(text)

if __name__ == '__main__':
    main()