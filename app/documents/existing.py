import logging
import dotenv
import os
from llama_index.core import StorageContext, load_index_from_storage, VectorStoreIndex
from .vectorstore import IRISVectorStore

logger = logging.getLogger(__name__)

def query_existing_document(name, query):
    dotenv.load_dotenv()
    
    CONNECTION_STRING = os.getenv("IRIS_CONNECTION_STRING")
    if not CONNECTION_STRING:
        logger.error("Connection string is not set. Please check your environment variables.")
        raise ValueError("Connection string is not set.")
    
    #table_name is name in lowercase with data_ prefix
    table_name = f"data_{name.lower()}"

    logger.debug(f"Connecting to vector store with name: {name}, table_name: {table_name}")
    
    vector_store = IRISVectorStore.from_params(
        connection_string=CONNECTION_STRING,
        table_name=name,
        embed_dim=1536,
    )
    
    
    try:
        logger.debug(f"Loading index from storage for document: {name}")
        index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
    except Exception as e:
        logger.error(f"Failed to load index from storage: {e}")
        raise ValueError("Failed to load index from storage.") from e
    
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return response
