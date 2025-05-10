from langchain.vectorstores import Chroma
from .embeddings import get_google_embedding

_chroma_vector_store = None

def get_chroma_vector_store():
    global _chroma_vector_store
    if _chroma_vector_store is None:
        _chroma_vector_store = Chroma(
            embedding_function=get_google_embedding(),
            persist_directory="database/chroma"  # tambahkan jika perlu persistensi
        )
    return _chroma_vector_store