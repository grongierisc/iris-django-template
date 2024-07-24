from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Document, Conversation
from .serializers import DocumentSerializer, ConversationSerializer
from .embedding import generate_embedding
from .rag import query_rag_model

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def perform_create(self, serializer):
        content = serializer.validated_data['content']
        embedding = generate_embedding(content)
        serializer.save(embedding=embedding)

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    @action(detail=False, methods=['post'])
    def query(self, request):
        prompt = request.data.get('prompt')
        #model_name = request.data.get('model_name')
        model_name = 'facebook/rag-token-nq'
        response, related_docs = query_rag_model(prompt, model_name)
        conversation = Conversation.objects.create(
            model_name=model_name,
            prompt=prompt,
            response=response
        )
        conversation.documents.set(related_docs)
        conversation.save()
        serializer = self.get_serializer(conversation)
        return Response(serializer.data)
