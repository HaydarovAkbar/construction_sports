from django.db import models
from utils.models import State, Region, District, Neighborhood
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from account.models import User


class Votes(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Ovozlar'))
    attr = models.CharField(max_length=255, verbose_name=_('Atribut'), null=True, blank=True)

    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Голосования')
        verbose_name = _('Голосование')
        db_table = 'votes'
