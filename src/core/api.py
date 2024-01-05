from rest_framework import routers
from django.urls import path, include

from account import views as account_views
from app import views as app_views

api = routers.DefaultRouter()

# account registeration urls
api.register(r'users', account_views.UserView, basename='users')

# app urls
api.register(r'construction', app_views.ConstructionView, basename='construction')
api.register(r'construction-type', app_views.ConstructionTypeView, basename='construction-type')
api.register(r'season', app_views.SeasonView, basename='season')
api.register(r'season-price', app_views.SeasonPriceView, basename='season-price')
api.register(r'basis', app_views.BasisView, basename='basis')



urlpatterns = [
    path('', include(api.urls)),
    path('account/login/', account_views.LoginApiView.as_view(), name='login'),
]