from django.contrib import admin
from .models import ConstructionType, Season, Basis, WhereIsBuilt, Construction, ConstructionImage

admin.site.register(ConstructionType)
admin.site.register(Season)
admin.site.register(Basis)
admin.site.register(WhereIsBuilt)
admin.site.register(Construction)
admin.site.register(ConstructionImage)