from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
dimension = model.get_sentence_embedding_dimension()

index = faiss.IndexFlatL2(dimension)
texts = []

def add_to_memory(text):
    vector = model.encode([text])[0]
    index.add(np.array([vector], dtype="float32"))
    texts.append(text)

def search_memory(query, top_k=3):
    if len(texts) == 0:
        return []

    vector = model.encode([query])[0]
    vector = np.array([vector], dtype="float32")
    distances, indices = index.search(vector, top_k)
    return [texts[i] for i in indices[0] if i < len(texts)]
