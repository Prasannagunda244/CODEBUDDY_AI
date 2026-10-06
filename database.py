import chromadb

from sentence_transformers import SentenceTransformer


# Create embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# Create ChromaDB
client = chromadb.PersistentClient(
    path="./chroma_db"
)


# Create collection
collection = client.get_or_create_collection(
    name="coding_knowledge"
)


def create_embedding(text):

    embedding = model.encode(text)

    return embedding.tolist()


def add_knowledge(text, item_id):

    embedding = create_embedding(text)

    collection.add(

        ids=[item_id],

        documents=[text],

        embeddings=[embedding]
    )


def search_knowledge(query):

    embedding = create_embedding(query)

    results = collection.query(

        query_embeddings=[embedding],

        n_results=3
    )

    return results