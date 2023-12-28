from django.db import models
from utils.models import State, Region, District, Neighborhood


class ConstructionType(models):
    title = models.CharField(max_length=255, verbose_name='Название')
    attr = models.CharField(max_length=255, verbose_name='Атрибут')

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Типы строительства'
        verbose_name = 'Тип строительства'
        db_table = 'construction_type'


class Season(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    attr = models.CharField(max_length=255, verbose_name='Атрибут')

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Сезоны'
        verbose_name = 'Сезон'
        db_table = 'season'


class SeasonPrice(models.Model):
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=14, decimal_places=2, verbose_name='Цена')
    construction_type = models.ForeignKey(ConstructionType, on_delete=models.SET_NULL, null=True)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'Цены сезонов'
        verbose_name = 'Цена сезона'
        db_table = 'season_price'

    def __str__(self):
        return self.price


class Basis(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    attr = models.CharField(max_length=255, verbose_name='Атрибут')

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Основания'
        verbose_name = 'Основание'
        db_table = 'basis'


class WhereIsBuilt(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    attr = models.CharField(max_length=255, verbose_name='Атрибут')

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Где строится'
        verbose_name = 'Где строится'
        db_table = 'where_is_built'


class Construction(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    construction_type = models.ForeignKey(ConstructionType, on_delete=models.SET_NULL, null=True)
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)
    basis = models.ForeignKey(Basis, on_delete=models.SET_NULL, null=True)
    where_is_built = models.ForeignKey(WhereIsBuilt, on_delete=models.SET_NULL, null=True)

    length = models.DecimalField(max_digits=14, decimal_places=2, verbose_name='Высота', null=True, blank=True)
    witdh = models.DecimalField(max_digits=14, decimal_places=2, verbose_name='Ширина', null=True, blank=True)
    height = models.DecimalField(max_digits=14, decimal_places=2, verbose_name='Длина', null=True, blank=True)

    is_active = models.BooleanField(default=True, verbose_name='Активный')
    is_deleted = models.BooleanField(default=False, verbose_name='Удаленный')

    longitude = models.DecimalField(max_digits=14, decimal_places=10, verbose_name='Долгота', null=True, blank=True)
    latitude = models.DecimalField(max_digits=14, decimal_places=10, verbose_name='Широта', null=True, blank=True)

    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    started_date = models.DateField(null=True, blank=True, verbose_name='Дата начала')
    ended_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')

    image = models.ImageField(upload_to='construction/', null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name_plural = 'Строительства'
        verbose_name = 'Строительство'
        db_table = 'construction'
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['construction_type']),
            models.Index(fields=['season']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return self.title
