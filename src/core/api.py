from rest_framework import routers
from django.urls import path, include

from account import views as account_views
from app import views as app_views

api = routers.DefaultRouter()

# account registeration urls
api.register(r'users', account_views.UserView, basename='users')


urlpatterns = [
    path('', include(api.urls)),
    path('account/login/', account_views.LoginApiView.as_view(), name='login'),
]