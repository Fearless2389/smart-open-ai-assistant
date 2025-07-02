# OLD (remove this)
# import faiss

# NEW (use sklearn for similarity search)
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Example replacement function
def build_index(embeddings):
    index = NearestNeighbors(n_neighbors=1, metric="cosine")
    index.fit(embeddings)
    return index

def rag_answer(query, docs, embed_fn):
    query_embedding = embed_fn([query])
    doc_embeddings = embed_fn(docs)

    index = build_index(doc_embeddings)
    _, indices = index.kneighbors(query_embedding)
    closest_doc = docs[indices[0][0]]

    return f"Answer based on: {closest_doc}"
