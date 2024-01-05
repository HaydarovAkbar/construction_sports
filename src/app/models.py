from django.db import models
from utils.models import State, Region, District, Neighborhood
from django.utils.translation import gettext_lazy as _


class ConstructionType(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Название'))
    attr = models.CharField(max_length=255, verbose_name=_('Атрибут'), null=True, blank=True)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    image = models.ImageField(upload_to='construction_type', verbose_name='Изображение', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_image_url(self):
        try:
            return self.image.url
        except:
            return ''

    class Meta:
        verbose_name_plural = _('Типы строительства')
        verbose_name = _('Тип строительства')
        db_table = 'construction_type'


class Season(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Название'))
    attr = models.CharField(max_length=255, verbose_name=_('Атрибут'), null=True, blank=True)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Сезоны')
        verbose_name = _('Сезон')
        db_table = 'season'


class SeasonPrice(models.Model):
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=14, decimal_places=2, verbose_name='Цена')
    construction_type = models.ForeignKey(ConstructionType, on_delete=models.SET_NULL, null=True)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = _('Цены сезонов')
        verbose_name = _('Цена сезона')
        db_table = 'season_price'

    def __str__(self):
        return self.price


class Basis(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Название'))
    attr = models.CharField(max_length=255, verbose_name=_('Атрибут'), null=True, blank=True)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Основания')
        verbose_name = _('Основание')
        db_table = 'basis'


class WhereIsBuilt(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Название'))
    attr = models.CharField(max_length=255, verbose_name=_('Атрибут'))

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Где строится')
        verbose_name = _('Где строится')
        db_table = 'where_is_built'


class Construction(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Название'))
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

    class Meta:
        verbose_name_plural = _('Строительства')
        verbose_name = _('Строительство')
        db_table = 'construction'
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['construction_type']),
            models.Index(fields=['season']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return self.title


class ConstructionImage(models.Model):
    image = models.ImageField(upload_to='construction', verbose_name='Изображение')
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name_plural = 'Изображения строительств'
        verbose_name = 'Изображение строительства'
        db_table = 'construction_image'

    def __str__(self):
        return str(self.created_at)


class SeasonStat(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    construction_type = models.ForeignKey(ConstructionType, on_delete=models.SET_NULL, null=True)
    count = models.IntegerField(verbose_name='Количество строительств')
    price = models.DecimalField(max_digits=14, decimal_places=2, verbose_name='Цена сезона (миллион сумов)')

    class Meta:
        verbose_name_plural = 'Статистика сезонов'
        verbose_name = 'Статистика сезона'
        db_table = 'season_stat'

    def __str__(self):
        return str(self.price)