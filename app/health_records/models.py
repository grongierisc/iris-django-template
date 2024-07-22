from django.db import models

class ElectronicHealthRecord(models.Model):
    patient_id = models.CharField(max_length=50)
    record_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
