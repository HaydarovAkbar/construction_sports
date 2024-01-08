from django_filters.rest_framework import DjangoFilterBackend


class SeasonStatFilterBackend(DjangoFilterBackend):
    def filter_queryset(self, request, queryset, view):
        season = request.query_params.get('season', None)
        basis = request.query_params.get('basis', None)
        if season:
            queryset = queryset.filter(season=season)
        if basis:
            queryset = queryset.filter(basis=basis)
        # user = request.user
        # if user.is_superuser:
        #     return queryset
        # else:
        #     return queryset.filter(user=user)
        return queryset