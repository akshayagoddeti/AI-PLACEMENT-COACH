import chromadb
from sentence_transformers import SentenceTransformer


# Create ChromaDB database
client = chromadb.PersistentClient(path="vectorstore")

# Create or get collection
collection = client.get_or_create_collection(
    name="study_material"
)

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def chunk_text(text, chunk_size=500, overlap=50):
    """
    Split large text into smaller chunks.
    """

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(words[start:end])

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def add_document(text, document_name):
    """
    Add document chunks to ChromaDB.
    """

    chunks = chunk_text(text)

    embeddings = embedding_model.encode(chunks).tolist()

    ids = [
        f"{document_name}_{i}"
        for i in range(len(chunks))
    ]

    # Check whether this document is already stored
    existing = collection.get(
        ids=ids
    )

    existing_ids = set(existing["ids"])

    new_ids = []
    new_chunks = []
    new_embeddings = []

    for i in range(len(chunks)):

        if ids[i] not in existing_ids:

            new_ids.append(ids[i])
            new_chunks.append(chunks[i])
            new_embeddings.append(embeddings[i])

    if new_ids:

        collection.add(
            ids=new_ids,
            documents=new_chunks,
            embeddings=new_embeddings
        )

    return len(new_chunks)

def search_documents(question, number_of_results=3):
    """
    Search ChromaDB for relevant information.
    """

    question_embedding = embedding_model.encode(
        [question]
    ).tolist()

    results = collection.query(
        query_embeddings=question_embedding,
        n_results=number_of_results
    )

    return results["documents"][0]