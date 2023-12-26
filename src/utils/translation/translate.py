from modeltranslation.translator import translator, TranslationOptions, register
from ..models import State


@register(State)
class StateTranslationOptions(TranslationOptions):
    fields = ('name',)


# @register(Category)
# class CategoryTranslationOptions(TranslationOptions):
#     fields = ('shortname', 'fullname')
#
#
# @register(Specialization)
# class SpecializationTranslationOptions(TranslationOptions):
#     fields = ('shortname', 'fullname')
#
#
# @register(Region)
# class RegionTranslationOptions(TranslationOptions):
#     fields = ('shortname', 'fullname')
#
#
# @register(District)
# class DistrictTranslationOptions(TranslationOptions):
#     fields = ('shortname', 'fullname')
#
#
# @register(Instruction)
# class InstructionTranslationOptions(TranslationOptions):
#     fields = ('file_name', 'content')