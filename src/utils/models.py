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
