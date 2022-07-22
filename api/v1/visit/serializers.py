from rest_framework import serializers
from ..patient.serializers import PatientSerializer
from api.v1.visit.models import Visit


class VisitSerializer(serializers.ModelSerializer):

    patient = PatientSerializer(read_only=True)

    class Meta:
        model = Visit
        fields = ["id", "visit_reason", "visit_date", "created_at", "updated_at", "patient", ]
