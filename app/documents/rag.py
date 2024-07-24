import os
from dotenv import load_dotenv
from llama_index.core import StorageContext
from llama_index.core import VectorStoreIndex
from llama_iris import IRISVectorStore
from .models import Document
from .embedding import generate_embedding

#load_dotenv(override=True)

IRIS_CONNECTION_STRING = os.getenv("IRIS_CONNECTION_STRING")

def query_rag_model(prompt, model_name):
    documents = Document.objects.all()
    vector_store = IRISVectorStore.from_params(
        connection_string=IRIS_CONNECTION_STRING,
        table_name="documents",
        embed_dim=768,  # Assuming BAAI/bge-small-en-v1.5 embedding dimension
    )
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
        show_progress=True,
    )
    query_engine = index.as_query_engine()
    response = query_engine.query(prompt)
    related_docs = perform_vector_search(generate_embedding(prompt))
    return str(response), related_docs

def perform_vector_search(embedding):
    connection = iris.connect("localhost:1972/USER", "_system", "SYS")
    cursor = connection.cursor()
    query = """
    SELECT UID, Embedding FROM Sample.Embeddings
    ORDER BY VECTOR_DOT_PRODUCT(Embedding, TO_VECTOR(?,double)) DESC
    LIMIT 5
    """
    params = [str(embedding)]
    cursor.execute(query, params)
    related_docs = []
    for row in cursor:
        uid = row[0]
        doc = Document.objects.get(id=uid)
        related_docs.append(doc)
    return related_docs
