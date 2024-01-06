from drf_yasg import openapi

season_stat_list = [
    openapi.Parameter('season', openapi.IN_BODY, description="season", type=openapi.TYPE_INTEGER,
                      required=True),
    openapi.Parameter('construction_type', openapi.IN_BODY, description="construction_type", type=openapi.TYPE_INTEGER),
]
