from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
import os
from django.conf import settings


# Import the Post and Comment models
from community.models import Post, Comment

# Import the Post and Comment serializers
from community.serializers import PostSerializer, CommentSerializer

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

def index(request):
    with open(os.path.join(settings.BASE_DIR, 'static/index.html')) as f:
        return HttpResponse(f.read())