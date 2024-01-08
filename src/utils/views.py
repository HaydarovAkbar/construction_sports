from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.translation import activate
from rest_framework.permissions import IsAuthenticated

from . import models
from . import pagination
from . import serializers


class StateViewSet(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer
    pagination_class = pagination.TenPagination

    # permission_classes = [IsAuthenticated, ]


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = models.Language.objects.all()
    serializer_class = serializers.LanguageSerializer
    pagination_class = pagination.TenPagination

    # permission_classes = [IsAuthenticated, ]


class RegionViewSet(viewsets.ModelViewSet):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer
    pagination_class = pagination.TenPagination

    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['shortname', 'inn', ]
    permission_classes = [IsAuthenticated, ]


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer
    pagination_class = pagination.TenPagination

    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['shortname', 'inn', ]
    permission_classes = [IsAuthenticated, ]
