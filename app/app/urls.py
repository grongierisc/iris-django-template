from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from community.views import PostViewSet, CommentViewSet

from sqloniris.views import index
from interop.views import index as interop_index

from documents.views import DocumentViewSet, ConversationViewSet
from health_records.views import EHRViewSet

from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'health_records', EHRViewSet)
router.register(r'conversations', ConversationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('iris/', index),
    path('interop/', interop_index),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
