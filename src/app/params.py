from drf_yasg import openapi

construction_type_enter = [
    openapi.Parameter('image', openapi.IN_BODY, description="Choose file", type=openapi.TYPE_FILE, required=True),
    openapi.Parameter('title', openapi.IN_BODY, description="title", type=openapi.TYPE_STRING,
                      required=True),
    openapi.Parameter('title_uz', openapi.IN_BODY, description="title_uz", type=openapi.TYPE_STRING, required=True),
    openapi.Parameter('title_ru', openapi.IN_BODY, description="title_ru", type=openapi.TYPE_STRING,
                      required=True),
    openapi.Parameter('title_en', openapi.IN_BODY, description="title_en", type=openapi.TYPE_STRING),
    openapi.Parameter('attr', openapi.IN_BODY, description="attr", type=openapi.TYPE_STRING),
]
