from rest_framework import serializers

from .models import Season, SeasonPrice, ConstructionType, Basis, Construction, SeasonStat, WhereIsBuilt


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'


class SeasonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ('id', 'title', 'attr',)


class SeasonPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonPrice
        fields = '__all__'


class ConstructionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionType
        fields = '__all__'


class ConstructionTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstructionType
        fields = ('id', 'title', 'attr',)


class BasisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basis
        fields = '__all__'


class BasisListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basis
        fields = ('id', 'title', 'attr',)


class WhereIsBuiltSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhereIsBuilt
        fields = '__all__'


class ConstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Construction
        fields = '__all__'


class SeasonStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonStat
        fields = '__all__'
