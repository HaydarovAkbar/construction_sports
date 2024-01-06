from django.contrib import admin
from .models import ConstructionType, Season, Basis, WhereIsBuilt, Construction, ConstructionImage, SeasonStat

admin.site.register(ConstructionType)
admin.site.register(Season)
admin.site.register(Basis)
admin.site.register(WhereIsBuilt)
admin.site.register(Construction)
admin.site.register(ConstructionImage)
admin.site.site_header = 'Qurilish sport Admin panel'
admin.site.site_title = 'Qurilish sport Admin panel'
admin.site.index_title = 'Qurilish sport Admin panel'
admin.site.register(SeasonStat)
