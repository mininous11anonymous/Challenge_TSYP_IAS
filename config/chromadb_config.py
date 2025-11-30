import os
import chromadb

def init_chroma():
    """Initialize and return the ChromaDB collection."""
    chroma_path = os.getenv("CHROMA_PATH")

    client = chromadb.PersistentClient(path=chroma_path)
    collection = client.get_or_create_collection(
        name="industry_knowledge"
    )
    return collection
