# modules/retriever.py

import faiss
from sentence_transformers import SentenceTransformer
import fitz  # PyMuPDF
import numpy as np

# Load the embedding model (you can use others like 'all-mpnet-base-v2')
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def extract_text_from_pdf(file) -> str:
    """
    Extracts plain text from a PDF file using PyMuPDF.
    Returns the full extracted text.
    """
    doc = fitz.open(stream=file.read(), filetype="pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

def chunk_text(text: str, chunk_size: int = 300) -> list:
    """
    Splits text into smaller chunks for better embedding and retrieval.
    """
    words = text.split()
    chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

def build_vector_store(chunks: list):
    """
    Creates a FAISS index from embedded text chunks.
    Returns the index and the original chunk list.
    """
    embeddings = embedder.encode(chunks)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))
    return index, chunks

def retrieve_relevant_chunks(index, chunks, query: str, top_k: int = 3) -> list:
    """
    Returns the top_k most relevant text chunks for the user's query.
    """
    query_embedding = embedder.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)
    return [chunks[i] for i in indices[0]]

def rag_answer(file) -> list:
    """
    Full RAG pipeline: extract text from file → chunk → embed → store → return chunks.
    Returns the list of chunks to use as context for the main LLM.
    """
    text = extract_text_from_pdf(file)
    chunks = chunk_text(text)
    index, chunk_list = build_vector_store(chunks)
    return chunk_list  # stored for use with future queries
