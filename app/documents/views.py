from django.http import JsonResponse
import logging
from django import forms
import json
import openai
import dotenv

from llama_index.core import VectorStoreIndex, Document, StorageContext, load_index_from_storage
#import openai
from .vectorstore import IRISVectorStore
import os

from .models import Document as LocalDocument
from .existing import query_existing_document



def index(request):
    logger = logging.getLogger(__name__)
    dotenv.load_dotenv()
    json_data = json.loads(request.body)
    query = json_data["query_text"]

 
    responses = []
    if "selected_documents" in json_data:
        selected_documents = json_data["selected_documents"] 
        for doc in selected_documents:
            response = query_existing_document(doc, query)
            responses.append(response)
    else:
        selected_documents = []

    
    

    #create a new document with the Document class
    if json_data["document_text"] != "" and json_data["document_name"] != "":
        document = json_data["document_text"]
        document_name = json_data["document_name"]
        newdoc = LocalDocument(name=document_name, content=document)
        newdoc.save()

        text_list = [document]
        documents = [Document(text=t) for t in text_list]

        CONNECTION_STRING = os.getenv("IRIS_CONNECTION_STRING")
        
        vector_store = IRISVectorStore.from_params(
            connection_string=CONNECTION_STRING,
            table_name=document_name,
            embed_dim=1536,
        )

        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        # build index
        index = VectorStoreIndex.from_documents(
            documents, 
            storage_context=storage_context, 
            show_progress=False, 
        )

        logger.debug(f"Index created and stored successfully for document: {document_name}")

        query_engine = index.as_query_engine()
        try:
            response = query_engine.query(query)
            responses.append(response)
        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            return JsonResponse({"error": "An unexpected error occurred"}, status=500)
    
    existing_document_names = [doc.name for doc in LocalDocument.objects.all()]

    formatted_responses = []
    citations = []
    for response in responses:
        formatted_responses.append(response.response)
        citations.append(response.get_formatted_sources(1000))

    return JsonResponse({"responses": formatted_responses, 
                         "citations": citations, 
                         "existing_document_names": existing_document_names}, status=200)
    


    
def get_documents(request):
    #get all existing document names from the database
    existing_document_names = [doc.name for doc in LocalDocument.objects.all()]
    return JsonResponse({"existing_document_names": existing_document_names}, status=200)