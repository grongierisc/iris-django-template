from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from interop.views import index as interop_index

from documents.views import index as documents_index
from documents.views import get_documents

from django.views.generic import TemplateView


router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('interop/', interop_index),
    path('api/documents/', documents_index),
    path('api/document_names/', get_documents),
    path('documents/', TemplateView.as_view(template_name='index.html')),
]
