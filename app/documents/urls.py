from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet, ConversationViewSet

router = DefaultRouter()
router.register(r'documents', DocumentViewSet)
router.register(r'conversations', ConversationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
