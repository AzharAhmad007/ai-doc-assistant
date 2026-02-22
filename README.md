# 🤖 AI Document Assistant — Quick Rebuild Reference

A lightweight **AI-powered document assistant** built using **FastAPI + LangChain + Ollama + FAISS**.  
It allows you to upload documents, embed them, and query them using local LLMs.

---

## 🚀 Features

- 📄 Multi-document upload (PDF supported)
- 🔍 Semantic search using FAISS vector store
- 🧠 Local LLM inference via Ollama
- ⚡ FastAPI backend with Swagger UI
- 🔁 Easy environment rebuild using `requirements.txt`

---

## 🛠️ Environment Setup

### 1️⃣ Create project folder
```bash
mkdir ai-doc-assistant && cd ai-doc-assistant
2️⃣ Create virtual environment
python3 -m venv venv
source venv/bin/activate        # Mac/Linux
3️⃣ Upgrade pip
pip install --upgrade pip
📦 Install Dependencies
pip install fastapi uvicorn langchain langchain-community langchain-ollama faiss-cpu pypdf python-multipart

Save dependencies:

pip freeze > requirements.txt
🔁 Rebuild Later from requirements.txt

If you delete your environment or move to another machine:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
🧠 Ollama Setup (One-Time System Install)

Install Ollama from:

https://ollama.com

Then run:

ollama pull llama3
ollama pull nomic-embed-text
ollama list

✔️ This downloads:

llama3 → LLM for answering questions

nomic-embed-text → embeddings model for vector search

📁 Project Structure
ai-doc-assistant/
│
├── main.py
├── requirements.txt
├── data/          # uploaded documents
├── indexes/       # FAISS vector indexes
└── venv/

Create folders:

mkdir data indexes
▶️ Run Server
python -m uvicorn main:app --reload --port 8001
