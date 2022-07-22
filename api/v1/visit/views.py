from rest_framework import viewsets

from api.v1.visit.models import Visit
from api.v1.visit.serializers import VisitSerializer


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes = []
