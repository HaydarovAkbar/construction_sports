from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# from django_filters.rest_framework import DjangoFilterBackend
from django.utils.translation import activate
from rest_framework.permissions import IsAuthenticated

from . import models
from . import pagination
from . import serializers


class StateViewSet(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer
    pagination_class = pagination.TenPagination

    # filter_backends = [OrganizationFilterBackend, ]
    # filterset_fields = ['shortname', 'inn', ]
    # permission_classes = [IsAuthenticated, ]
