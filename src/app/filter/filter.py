from django_filters.rest_framework import DjangoFilterBackend


class SeasonStatFilterBackend(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        try:
            user_lang = request.user.language.code
        except Exception:
            user_lang = 'ru'
        shortname = request.query_params.get('shortname', None)
        inn = request.query_params.get('inn', None)
        if shortname:
            if user_lang == 'ru':
                queryset = queryset.filter(shortname_ru__icontains=shortname)
            elif user_lang == 'en':
                queryset = queryset.filter(shortname_en__icontains=shortname)
            elif user_lang == 'uz':
                queryset = queryset.filter(shortname_uz__icontains=shortname)
            else:
                queryset = queryset.filter(shortname_oz__icontains=shortname)
        if inn:
            queryset = queryset.filter(inn__icontains=inn)
        user = request.user
        if user.is_superuser:
            return queryset
        else:
            return queryset.filter(user=user)
