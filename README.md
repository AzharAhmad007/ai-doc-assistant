AI Document Assistant —
Environment Setup:-
mkdir ai-doc-assistant && cd ai-doc-assistant
python3 -m venv venv
source venv/bin/activate        # Mac/Linux
pip install --upgrade pip


Install Dependencies:-
pip install fastapi uvicorn langchain langchain-community langchain-ollama faiss-cpu pypdf python-multipart
pip freeze > requirements.txt   # save after everything works
Rebuild From requirements.txt Later

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Ollama Setup (one-time system install)

# Download from https://ollama.com, then:
ollama pull llama3
ollama pull nomic-embed-text
ollama list                     # verify


mkdir data indexes
Run Server:- python -m uvicorn main:app --reload --port 8001
# App:     http://127.0.0.1:8001
# Swagger: http://127.0.0.1:8001/docs


