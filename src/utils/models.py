from django.db import models
from django.utils import timezone


class State(models.Model):
    name = models.CharField(max_length=255)
    attr = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'States'
        verbose_name = 'State'
        db_table = 'states'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(State, self).save(*args, **kwargs)
        return self


class Language(models.Model):
    name = models.CharField(max_length=255)
    attr = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Languages'
        verbose_name = 'Language'
        db_table = 'languages'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Language, self).save(*args, **kwargs)
        return self


class Region(models.Model):
    title = models.CharField(max_length=255)
    attr = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='regions', null=True, blank=True)

    erp_id = models.PositiveIntegerField(null=True, blank=True)
    soato_code = models.PositiveIntegerField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Regions'
        verbose_name = 'Region'
        db_table = 'regions'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Region, self).save(*args, **kwargs)
        return self


class District(models.Model):
    title = models.CharField(max_length=255)
    attr = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    region = models.ForeignKey(Region, on_delete=models.SET_NULL, related_name='districts', null=True, blank=True)

    erp_id = models.PositiveIntegerField(null=True, blank=True)
    soato_code = models.PositiveIntegerField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Districts'
        verbose_name = 'District'
        db_table = 'districts'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(District, self).save(*args, **kwargs)
        return self


class Neighborhood(models.Model):  # Mahalla / Квартал
    title = models.CharField(max_length=255)
    attr = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    district = models.ForeignKey(District, on_delete=models.SET_NULL, related_name='neighborhoods', null=True,
                                 blank=True)

    erp_id = models.PositiveIntegerField(null=True, blank=True)
    soato_code = models.PositiveIntegerField(null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Neighborhoods'
        verbose_name = 'Neighborhood'
        db_table = 'neighborhoods'

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(Neighborhood, self).save(*args, **kwargs)
        return self
