#Bibliothèques
import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#Partie-01 : Création de l'interface utilisateur

#Interface Utilisateur
st.header("Mon Assistant Personnel IA")

#Sidebar pour documents PDF
with st.sidebar:
    st.title("Vos documents")
    uploaded_file = st.file_uploader("Télécharger votre fichier PDF", type=["pdf"])


#PARTIE-02 : Traitement des documents PDF, extraction et découpe en morceaux (Chunks)

#Extraction du texte
if uploaded_file is not None:
    pdfReader = PdfReader(uploaded_file)
    text = ""
    for page in pdfReader.pages:
        text += page.extract_text()

#Découpe en Chunks
    textSplitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = textSplitter.split_text(text)


#PARTIE-03 : Générer & Stocker les Embeddings

#Générer les Embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

#Créer le Vector Store
    vectorStore = FAISS.from_texts(chunks, embeddings)


#PARTIE-04 : Récupérer & Analyer la question

#Récupérer la question
    userQuestion = st.text_input("Comment puis-je vous aider ?")

#Faire une recherche de correspondance (Similarity Search)
    if userQuestion:
        match = vectorStore.similarity_search(userQuestion)


#PARTIE-05 : Générer & Afficher la réponse

#définir le LLM
        llm = ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            temperature=0,
            max_tokens=1000,
            model="gpt-3.5-turbo"
        )

#Afficher la réponse
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents = match, question = userQuestion)
        st.write(response)
