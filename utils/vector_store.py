def store_chunks(collection, chunks):
    """Store text chunks inside ChromaDB."""
    for i, chunk in enumerate(chunks):
        if len(chunk.strip()) == 0:
            continue
        collection.add(
            ids=[f"chunk-{i}"],
            documents=[chunk]
        )
