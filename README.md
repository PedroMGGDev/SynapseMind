# 🧠 SynapseMind – AI Assistant with Semantic Memory

**SynapseMind** is an advanced conversational AI system built with a modular architecture, integrating a Large Language Model (LLM) from OpenAI with semantic memory powered by FAISS and sentence-transformers.

This project demonstrates expertise in:
- Prompt engineering
- Semantic embeddings
- Vector search with FAISS
- Contextual memory design
- Modular and scalable AI code architecture

---

## ⚙️ Architecture Overview

```
User Input
   ↓
Short-term Memory (Chat History)
   ↓
Semantic Memory (Vector Embeddings via FAISS)
   ↓
Combined Context
   ↓
LLM Call (GPT-3.5 Turbo via OpenAI API)
   ↓
Response
```

---

## 📦 Project Structure

```
SynapseMind/
├── main.py
├── core/
│   ├── llm_interface.py
│   ├── memory_manager.py
│   ├── semantic_memory.py
├── requirements.txt
├── README.md
```

---

## 🧠 Features

- Semantic memory with similarity search using FAISS
- Integration with OpenAI's GPT-3.5 for natural language generation
- Memory management to simulate evolving conversations
- Fully modular architecture
- Designed to run even on mobile devices via Google Colab

---

## 🚀 How to Use

Inside your Python script or Colab notebook:

```python
from SynapseMind.main import chat

print(chat("Hi, who are you?"))
print(chat("What's the capital of France?"))
print(chat("Do you remember what I said earlier?"))
```

---

## 🧪 Technologies Used

- `openai` (LLM integration)
- `faiss-cpu` (vector memory)
- `sentence-transformers` (`paraphrase-MiniLM-L6-v2` model for embeddings)
- Python 3.11+
- Google Colab

---

## 💻 Installation

To run locally:

```bash
pip install -r requirements.txt
```

To use in Colab:
- Upload all files and folders
- Run `main.py` or interact via notebook cells

---

## 📌 Notes

- Memory is stored in RAM using FAISS (non-persistent for now)
- All logic is contained in pure Python and does not depend on frontend frameworks

---

## 🧑‍💻 Author

Developed by **Pedro Miguel Gomes Guerrero**, focused on building AI-first architectures for cognitive interfaces.

> Designed not to look like an app, but like a brain.
