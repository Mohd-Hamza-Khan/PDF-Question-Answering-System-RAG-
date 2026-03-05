Below is a **clean, professional GitHub README** you can directly paste into your repository. It is written to look like **a strong AI/ML portfolio project**.

---

# 📄 PDF Question Answering System using RAG

An **AI-powered document question answering system** built using a **Retrieval-Augmented Generation (RAG)** pipeline.
The system allows users to **ask questions from PDF documents and receive accurate answers based strictly on the document content**.

It runs **completely locally**, ensuring **privacy, low cost, and fast inference**.

---

# 🚀 Features

✅ Query information from PDF documents
✅ Semantic search using vector embeddings
✅ Local LLM inference (no API required)
✅ Reduced hallucination with strict prompting
✅ Fast similarity search using vector database
✅ Context-aware question answering

---

# 🧠 Tech Stack

* 🧩 LangChain – LLM orchestration framework
* 🤖 Ollama – Run LLMs locally
* 📚 FAISS – Vector similarity search
* 🧠 Phi-3 Mini – Language model for answer generation
* 🔎 mxbai-embed-large – Embedding model for semantic search

---

# 🏗 System Architecture

```
PDF Documents
      │
      ▼
Document Loader
(PyPDFLoader)
      │
      ▼
Text Chunking
(RecursiveCharacterTextSplitter)
      │
      ▼
Embedding Generation
(mxbai-embed-large)
      │
      ▼
Vector Database
(FAISS)
      │
      ▼
Retriever
      │
      ▼
LLM (Phi3-mini)
      │
      ▼
Generated Answer
```

---

# 📂 Project Structure

```
project/
│
├── data/                  # Input PDF files
│
├── vectorestore/
│   └── db_faiss/          # Saved FAISS vector index
│
├── create_memory_for_llm.py              # Create embeddings and store in FAISS
│
├── connect_memory_with_llm.py               # Ask questions from documents
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/mohd-hamza-khan/PDF-Question-Answering-System-RAG-.git
cd pdf-rag-system
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Install and run Ollama

Install **Ollama**

```bash
https://ollama.com/download
```

---

### 4️⃣ Pull required models

```bash
ollama pull phi3:mini
ollama pull mxbai-embed-large
```

---

# 📊 Step 1: Create Vector Database

Run the ingestion script:

```bash
python ingest.py
```

This will:

1. Load PDFs
2. Split text into chunks
3. Generate embeddings
4. Store them in **FAISS**

Output:

```
Saved FAISS vector store to vectorestore/db_faiss successfully.
```

---

# 💬 Step 2: Query the Documents

Run the QA system:

```bash
python query.py
```

Example:

```
Write Query Here:
What is the main objective of the document?
```

Output:

```
Result: The main objective of the document is...
Sources: [Document metadata]
```

---

# ⚡ Model Configuration

### LLM Settings

| Parameter   | Value     |
| ----------- | --------- |
| Model       | phi3:mini |
| Temperature | 0.3       |
| Max tokens  | 100       |

Lower temperature ensures **more factual answers**.

---

# 📈 Performance

Approximate local performance:

| Model           | RAM     | Speed            |
| --------------- | ------- | ---------------- |
| Phi3-mini       | ~2.2 GB | 20–35 tokens/sec |
| Embedding Model | ~1.2 GB | Fast             |

Works smoothly on **mid-range laptops**.

---

# 🎯 Applications

This system can be used for:

📚 Research paper assistants
🏢 Enterprise knowledge base
⚖ Legal document search
🏥 Medical research analysis
📖 Educational study tools

---

# 🔮 Future Improvements

Planned upgrades:

* Hybrid search (BM25 + Vector Search)
* Reranking models
* Web UI using Streamlit
* Multi-document reasoning
* Advanced RAG pipelines
* Larger models like:

  * Mistral 7B
  * Llama 3


---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Submit a pull request

---


# 👨‍💻 Author

**MOhd Hamza Khan**

If you found this project useful, consider giving it a ⭐ on GitHub!

---

⭐ **Star the repo if you like it!**

---
