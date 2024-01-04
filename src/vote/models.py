from django.db import models
from utils.models import State, Region, District, Neighborhood
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from account.models import User
from app.models import Construction


class Votes(models.Model):
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Состояние'))
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Пользователь'))
    construction = models.ForeignKey(Construction, on_delete=models.SET_NULL, null=True, blank=True,
                                     verbose_name=_('Строительство'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('Голосования')
        verbose_name = _('Голосование')
        db_table = 'votes'
