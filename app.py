
import streamlit as st
import os
import time
import pandas as pd
import pickle

# openai
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI

# chunking
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_community.document_loaders.csv_loader import CSVLoader

# import getpass
# import os

# if not os.getenv("OPENAI_API_KEY"):
#     os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

# env
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY']= os.getenv("OPENAI_API_KEY")
API_KEY= os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=API_KEY,  
    # base_url="...",
    # organization="...",
    # other params...
)

from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_core.documents import Document
import nltk
nltk.download('punkt_tab')
nltk.data.find('tokenizers/punkt_tab')
nltk.download('averaged_perceptron_tagger') 
nltk.find('taggers/averaged_perceptron_tagger')

markdown_path = "Crustdata_Discovery_And_Enrichment_API.md"

# data = loader.load()
# assert len(data) == 1
# assert isinstance(data[0], Document)
# readme_content = data[0].page_content
# print(readme_content[:250])

prompt=ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate respone based on the question
    <context>
    {context}
    <context>
    Question:{input}

    """

)

def create_vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings= OpenAIEmbeddings(
        model="text-embedding-3-small",
        # With the `text-embedding-3` class
        # of models, you can specify the size
        # of the embeddings you want returned.
        # dimensions=1024
    )

        st.session_state.loader = UnstructuredMarkdownLoader(markdown_path, mode="elements")

        st.session_state.docs=st.session_state.loader.load() ## Document Loading
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
        st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs[:50])
        st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings)

        # Save embeddings as a list of vectors
        embeddings_list = [i for i in st.session_state.final_documents]
        with open('embeddings.pkl', 'wb') as f:
            pickle.dump(embeddings_list, f)



st.title("RAG Document Q&A With Groq And Lama3")

user_prompt=st.text_input("Enter your query from the research paper")

if st.button("Document Embedding"):
    create_vector_embedding()
    st.write("Vector Database is ready")


if user_prompt:
    document_chain=create_stuff_documents_chain(llm,prompt)
    retriever=st.session_state.vectors.as_retriever()
    retrieval_chain=create_retrieval_chain(retriever,document_chain)

    start=time.process_time()
    response=retrieval_chain.invoke({'input':user_prompt})
    print(f"Response time :{time.process_time()-start}")

    st.write(response['answer'])

    ## With a streamlit expander
    with st.expander("Document similarity Search"):
        for i,doc in enumerate(response['context']):
            st.write(doc.page_content)
            st.write('------------------------')
