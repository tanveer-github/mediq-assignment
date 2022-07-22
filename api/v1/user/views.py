from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.v1.user.models import User
from api.v1.user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
