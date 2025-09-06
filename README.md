PDF RAG App · FAISS + LangChain

This app builds a Retrieval-Augmented Generation (RAG) system that ingests PDFs, indexes them with FAISS, and answers questions by retrieving relevant document snippets.

✨ Features
	•	📄 Ingest multiple PDFs from Docs/ (recursive)
	•	🔍 Chunking + embeddings → FAISS vector index on disk
	•	🧠 Simple question-answering based on indexed content
	•	⚡ Caching & configurable chunk sizes/overlap
	•	🧪 Simple evaluation harness (manual Q/A set)

⸻

🧱 Project Structure

.
├─ ingest.py                  # Ingest PDFs → FAISS index
├─ rag_chain.py               # Chains, prompts, retrieval logic
├─ utils.py                   # Helpers: I/O, text utils, caching
├─ requirements.txt
├─ Docs/                      # Put your PDFs here
├─ index/                     # Persisted FAISS store
├─ eval/
│   ├─ questions.jsonl        # [{"question": "...", "answer": "..."}]
│   └─ run_eval.py
└─ README.md


⸻

⚙️ Prerequisites
	•	Python 3.10+
	•	Basic build tools (for FAISS CPU)

⸻

🔑 Environment Variables

Use one of the following:

Option A: .env file (local dev)

EMBED_MODEL=text-embedding-3-small
CHUNK_SIZE=1200
CHUNK_OVERLAP=150
TOP_K=4


⸻

📦 Install

# Create venv
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
.\.venv\Scripts\activate

# Install deps
pip install -r requirements.txt

Minimal requirements.txt (edit if you already have one):

langchain
faiss-cpu
pypdf
python-dotenv


⸻

📥 Ingest PDFs

Put all PDFs in Docs/ then run:

python ingest.py

This will:
	1.	Load PDFs from Docs/ (recursively)
	2.	Chunk & embed
	3.	Save FAISS index under index/

⸻

🧩 How It Works (RAG Pipeline)
	1.	Load PDFs → PyPDFLoader
	2.	Split documents → RecursiveCharacterTextSplitter
	3.	Embed chunks → custom embedding model (e.g., OpenAI, HuggingFace)
	4.	Index with FAISS (persisted)
	5.	Retrieve top-K chunks per query
	6.	Generate answer based on retrieved context
	7.	Cite sources with page numbers and snippets

Prompt (simplified) in rag_chain.py:
	•	System: “Answer with citations from provided context; say ‘I don’t know’ if not found.”
	•	User: question
	•	Context: top-K chunks (title, page, snippet)

⸻

🧪 Quick Eval (Optional)

Add a few Q/A pairs to eval/questions.jsonl:

{"question":"What is the warranty policy?", "answer":"..."}

Run:

python eval/run_eval.py

Outputs naive accuracy & saves model answers for review.

⸻

🚀 Deployment (Optional)

For server or local deployment, you can create a simple web service or run the app locally using Flask or FastAPI to handle incoming questions.

⸻

🛠️ Configuration

Tweak via env vars or constants in rag_chain.py:
	•	CHUNK_SIZE, CHUNK_OVERLAP → controls recall/latency
	•	TOP_K → retrieval breadth
	•	EMBED_MODEL → embedding model

⸻

🔧 Troubleshooting
	•	FAISS not found → ensure faiss-cpu installed (no GPU needed)
	•	No answers / hallucinations → increase TOP_K, reduce temperature, improve chunk size
	•	Duplicate chunks → clean Docs/, delete index/, re-ingest
	•	Large PDFs slow → raise CHUNK_SIZE moderately and cache embeddings

⸻

🗺️ Roadmap
	•	Add reranking (e.g., BGE-Reranker)
	•	Add citations highlighting in UI
	•	Add confidence scoring & feedback buttons
	•	Add basic eval dashboard

⸻

📸 Screenshots (optional)

/assets/
  home.png
  answer_with_citations.png

Embed in README once you capture them:

![Home](assets/home.png)
![Answer](assets/answer_with_citations.png)


⸻

📝 License

MIT — feel free to use and modify.

⸻

🙏 Acknowledgements
	•	LangChain
	•	FAISS
