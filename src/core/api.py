from rest_framework import routers
from django.urls import path, include

api = routers.DefaultRouter()

urlpatterns = [
    path('', include(api.urls)),
    # path('account/login/', account_views.LoginApiView.as_view(), name='login'),
]