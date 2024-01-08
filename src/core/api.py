from rest_framework import routers
from django.urls import path, include

from account import views as account_views
from app import views as app_views
from utils import views as utils_views

api = routers.DefaultRouter()

# account registeration urls
api.register(r'users', account_views.UserView, basename='users')

# app urls
api.register(r'construction', app_views.ConstructionView, basename='construction')
api.register(r'construction-type', app_views.ConstructionTypeView, basename='construction-type')
api.register(r'season', app_views.SeasonView, basename='season')
api.register(r'season-price', app_views.SeasonPriceView, basename='season-price')
api.register(r'basis', app_views.BasisView, basename='basis')
api.register(r'where-is-built', app_views.WhereIsBuiltView, basename='where-is-built')
# api.register(r'construction-image', app_views.ConstructionImageView, basename='construction-image')
api.register(r'season-stat', app_views.SeasonStatView, basename='season-stat')

# utils urls
api.register(r'state', utils_views.StateViewSet, basename='state')
api.register(r'language', utils_views.LanguageViewSet, basename='language')
api.register(r'region', utils_views.RegionViewSet, basename='region')
api.register(r'district', utils_views.DistrictViewSet, basename='district')

urlpatterns = [
    path('', include(api.urls)),
    path('account/login/', account_views.LoginApiView.as_view(), name='login'),
]
