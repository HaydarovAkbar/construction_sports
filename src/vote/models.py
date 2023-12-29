from django.db import models
from utils.models import State, Region, District, Neighborhood
from accounts.models import User


class Votes(models.Model):
    title = models.CharField(max_length=255, verbose_name='Ovozlar')
    attr = models.CharField(max_length=255, verbose_name='Atribut', null=True, blank=True)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Голосования'
        verbose_name = 'Голосование'
        db_table = 'votes'
