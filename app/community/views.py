from django.shortcuts import render
from rest_framework import viewsets

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