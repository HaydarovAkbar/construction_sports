from django.contrib import admin
from django.urls import path, include
from .api import urlpatterns as api_urls
from django.conf.urls.i18n import i18n_patterns
from .yasg import schema_view
# bot url
# from bot.views import MainView as BotMainView

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    # path('bot/', BotMainView.as_view()),
]

urlpatterns += i18n_patterns(
    path('api/v1/', include(api_urls)),
)