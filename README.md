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

python3 -m venv venv
source venv/bin/activate        # Mac/Linux
