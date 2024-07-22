from rest_framework import serializers
from .models import ElectronicHealthRecord

class EHRSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectronicHealthRecord
        fields = '__all__'
