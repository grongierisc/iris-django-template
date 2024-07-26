from django.http import JsonResponse
import logging
from django import forms
import json
import openai
import dotenv
import re

from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core import Document as LlamaDocument
#import openai
from .vectorstore import IRISVectorStore
import os

from llama_index.core import VectorStoreIndex, get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor

from llama_index.llms.openai import OpenAI
from llama_index.core import Settings as LlamaSettings

from .models import Document 
from .existing import query_existing_document, get_clean_name



def index(request):
    logger = logging.getLogger(__name__)
    dotenv.load_dotenv()
    try:
        json_data = json.loads(request.body)
    except json.JSONDecodeError:
        logger.error("Invalid JSON received in request.")
        return JsonResponse({"error": "Invalid JSON format"}, status=400)
    

    query = json_data.get("query_text", "Describe the document")
    model_name = json_data.get("model_name", "gpt-4o-mini")
    temperature = json_data.get("temperature", 0.5)  # Default temperature is 0.5
    responses = {}

    llm = OpenAI(model=model_name, temperature=temperature)
    LlamaSettings.llm = llm

    selected_documents = json_data.get("selected_documents", [])
    for doc in selected_documents:
        try:
            response = query_existing_document(doc, query)
            responses[doc] = {
                "response": response.response,
                "citations": response.get_formatted_sources(1000)
            }
        except Exception as e:
            logger.error(f"Error querying document {doc}: {str(e)}")
            responses[doc] = {"error": "Failed to query document"}


    if json_data["document_text"] != "" and json_data["document_name"] != "":
        document_text = json_data["document_text"]
        document_name = json_data["document_name"]
        #substitute all kinds of whitespace with underscore using regular expressions
        document_name = get_clean_name(document_name)

        newdoc = Document(name=document_name, content=document_text)
        newdoc.save()

        documents = [LlamaDocument(text=document_text)]

        CONNECTION_STRING = os.getenv("IRIS_CONNECTION_STRING")
        
        vector_store = IRISVectorStore.from_params(
            connection_string=CONNECTION_STRING,
            table_name=document_name,
            embed_dim=1536,
        )

        storage_context = StorageContext.from_defaults(vector_store=vector_store)



        # build index
        try:
            index = VectorStoreIndex.from_documents(
                documents,
                storage_context=storage_context,
                show_progress=False,
            )

            logger.debug(f"Index created and stored successfully for document: {document_name}")

            retriever = VectorIndexRetriever(
                index=index,
                similarity_top_k=10,
            )

            # configure response synthesizer
            response_synthesizer = get_response_synthesizer()

            # assemble query engine
            query_engine = RetrieverQueryEngine(
                retriever=retriever,
                response_synthesizer=response_synthesizer,
                node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.7)],
            )
            response = query_engine.query(query)

            responses[document_name] = {
                "response": response.response,
                "citations": response.get_formatted_sources(1000)
            }

        except Exception as e:
            logger.error(f"Error creating or querying index for document {document_name}: {str(e)}")
            responses[document_name] = {"error": "Failed to create or query index"}

    # Fetch existing document names
    existing_document_names = [doc.name for doc in Document.objects.all()]

    return JsonResponse({
        "responses": responses,
        "existing_document_names": existing_document_names
    }, status=200)
    


    
def get_documents(request):
    #get all existing document names from the database
    existing_document_names = [doc.name for doc in Document.objects.all()]
    return JsonResponse({"existing_document_names": existing_document_names}, status=200)

def delete_documents(request):
    dotenv.load_dotenv()
    try:
        json_data = json.loads(request.body)
        document_names = json_data.get("document_names", [])

        if not document_names:
            return JsonResponse({"error": "No document names provided"}, status=400)

        # Initialize the vector store
        CONNECTION_STRING = os.getenv("IRIS_CONNECTION_STRING")
        if not CONNECTION_STRING:
            return JsonResponse({"error": "IRIS_CONNECTION_STRING not set"}, status=500)

        # Drop tables and delete local documents
        for name in document_names:
            name = get_clean_name(name)
            table_name = f"data_{name.lower()}"

            # Drop the corresponding table
            
            try:
                vector_store = IRISVectorStore.from_params(
                    connection_string=CONNECTION_STRING,
                    table_name=name,
                    embed_dim=1536,
                    perform_setup=False
                )
                vector_store.drop_table()
            except Exception as sql_error:
                return JsonResponse({"error": f"Failed to drop table {table_name}: {str(sql_error)}"}, status=500)

            # Debugging: Log the type and value of the name variable
            logging.debug(f"Type of name: {type(name)}, Value of name: {name}")

            # Ensure name is a string
            if isinstance(name, str):
                try:
                    all_documents = Document.objects.all()
                    for doc in all_documents:
                        if doc.name == name:
                            doc.delete()

                except Exception as orm_error:
                    return JsonResponse({"error": f"Failed to delete document {name}: {str(orm_error)}"}, status=500)
            else:
                logging.error("The name variable is not a string.")
                return JsonResponse({"error": "Invalid document name type"}, status=400)

        return JsonResponse({"status": "success", "message": "Documents and tables deleted successfully"})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)
    except Exception as e:
        return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)
