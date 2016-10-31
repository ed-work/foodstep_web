from rest_framework import viewsets
from django.contrib.auth.models import User

from .serializers import UserSerilizer


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerilizer
    queryset = User.objects.all()
