from modeltranslation.translator import translator, TranslationOptions, register
from ..models import State, Region, District, Neighborhood


@register(State)
class StateTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Region)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(District)
class SpecializationTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Neighborhood)
class RegionTranslationOptions(TranslationOptions):
    fields = ('title',)