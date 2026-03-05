from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
# from langchain_chroma import Chroma


# 1. load raw pdf

DATA_PATH = "data/"
def load_pdf(data):
    loader = DirectoryLoader(data,
                             glob="*.pdf",
                             loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents

documents = load_pdf(DATA_PATH)
# print(f"Loaded {len(documents)} documents from {DATA_PATH}")



# 2. create chunks
def create_chunks(extract_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(extract_data)
    return chunks

chunks = create_chunks(documents)
# print(f"Split into {len(chunks)} chunks")


# 4. store embeddings in FAISS
def store_embeddings(chunks):
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    db = FAISS.from_documents(chunks, embeddings)
    return db


db = store_embeddings(chunks)
DB_FAISS_PATH = "vectorestore/db_faiss"
db.save_local(DB_FAISS_PATH)
print(f"Saved FAISS vector store to {DB_FAISS_PATH} successfully.")