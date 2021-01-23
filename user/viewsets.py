
from rest_framework import viewsets
from . import models
from user.serializers import UserSerializer
from rest_framework.filters import SearchFilter


class UserViewset(viewsets.ModelViewSet):
    queryset = models.Userapp.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['phone']
