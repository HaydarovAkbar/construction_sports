from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from django.utils.translation import activate

from . import models
from . import serializers
from . import params

from utils.pagination.base import TenPagination, TwentyPagination, FiftyPagination


class ConstructionTypeView(viewsets.ModelViewSet):
    queryset = models.ConstructionType.objects.all()
    serializer_class = serializers.ConstructionTypeSerializer
    pagination_class = TenPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ConstructionTypeListSerializer
        return serializers.ConstructionTypeSerializer

    @swagger_auto_schema(manual_parameters=params.construction_type_enter, responses={201: 'Created'},
                         operation_id='Enter fields', operation_description='Enter fields')
    def create(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SeasonView(viewsets.ModelViewSet):
    queryset = models.Season.objects.all()
    serializer_class = serializers.SeasonSerializer
    pagination_class = TenPagination
    http_method_names = ['get', ]

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.SeasonListSerializer
        return serializers.SeasonSerializer


class SeasonPriceView(viewsets.ModelViewSet):
    queryset = models.SeasonPrice.objects.all()
    serializer_class = serializers.SeasonPriceSerializer
    pagination_class = TenPagination


class BasisView(viewsets.ModelViewSet):
    queryset = models.Basis.objects.all()
    serializer_class = serializers.BasisSerializer
    pagination_class = TenPagination
    http_method_names = ['get', ]

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.SeasonListSerializer
        return serializers.SeasonSerializer


class ConstructionView(viewsets.ModelViewSet):
    queryset = models.Construction.objects.all()
    serializer_class = serializers.ConstructionSerializer
    pagination_class = TenPagination


class WhereIsBuiltView(viewsets.ModelViewSet):
    queryset = models.WhereIsBuilt.objects.all()
    serializer_class = serializers.WhereIsBuiltSerializer
    pagination_class = TenPagination


class SeasonStatView(viewsets.ModelViewSet):
    queryset = models.SeasonStat.objects.all()
    serializer_class = serializers.SeasonStatSerializer
    pagination_class = TenPagination
