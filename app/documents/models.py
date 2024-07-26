#a documents model to store the documents

from django.db import models

class Document(models.Model):
    doc_id = models.CharField(max_length=255)
    name = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

