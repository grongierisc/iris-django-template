from rest_framework import viewsets
from .models import ElectronicHealthRecord
from .serializers import EHRSerializer

class EHRViewSet(viewsets.ModelViewSet):
    queryset = ElectronicHealthRecord.objects.all()
    serializer_class = EHRSerializer
