from rest_framework import viewsets

from api.v1.patient.models import Patient
from api.v1.patient.serializers import PatientSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = []
