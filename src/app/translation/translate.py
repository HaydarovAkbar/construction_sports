from modeltranslation.translator import TranslationOptions, register
from ..models import ConstructionType, Season, Basis, WhereIsBuilt, Construction


@register(ConstructionType)
class StateTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Season)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Basis)
class SpecializationTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(WhereIsBuilt)
class RegionTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Construction)
class RegionTranslationOptions(TranslationOptions):
    fields = ('title',)
