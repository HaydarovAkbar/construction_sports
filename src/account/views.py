from . import serializers
from . import models
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from utils.pagination import TenPagination


class LoginApiView(TokenObtainPairView):
    """The class is responsible for LpgIn functionality and Tokenaization"""
    serializer_class = serializers.LogInSerializer


class UserView(viewsets.ModelViewSet):
    """The class is responsible for User CRUD functionality"""
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializers
    pagination_class = TenPagination
