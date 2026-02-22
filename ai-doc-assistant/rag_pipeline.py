import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_classic.chains import RetrievalQA

INDEX_PATH = "indexes/faiss_index"

vector_store = None

embeddings = OllamaEmbeddings(model="nomic-embed-text")


def load_existing_index():
    global vector_store

    if os.path.exists(INDEX_PATH):
        vector_store = FAISS.load_local(
            INDEX_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )
        print("Loaded existing FAISS index from disk.")
    else:
        print("No existing index found.")


def create_vector_store(file_path: str):
    global vector_store

    # Load existing index if available
    if vector_store is None:
        load_existing_index()

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # Add metadata (important for multi-doc support)
    for doc in documents:
        doc.metadata["source"] = os.path.basename(file_path)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    docs = text_splitter.split_documents(documents)

    if vector_store is None:
        # First document ever
        vector_store = FAISS.from_documents(docs, embeddings)
    else:
        # Append new documents
        vector_store.add_documents(docs)

    # Save updated index
    vector_store.save_local(INDEX_PATH)

    return f"{os.path.basename(file_path)} indexed successfully."


def ask_question(question: str):
    global vector_store

    if vector_store is None:
        load_existing_index()

    if vector_store is None:
        return "No document indexed. Please upload a document first."

    llm = ChatOllama(model="llama3")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever(),
        return_source_documents=False
    )

    result = qa_chain.invoke({"query": question})

    return result["result"]