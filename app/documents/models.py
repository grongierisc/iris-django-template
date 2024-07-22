from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    embedding = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Conversation(models.Model):
    model_name = models.CharField(max_length=100)
    prompt = models.TextField()
    response = models.TextField()
    documents = models.ManyToManyField(Document)
    created_at = models.DateTimeField(auto_now_add=True)
