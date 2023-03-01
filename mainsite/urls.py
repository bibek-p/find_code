from . import views
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', views.index, name="index-page"),
    path('region/<country_name>/', views.list_of_region, name="index-page"),
    path('region/<country_name>/<state_name>', views.list_of_region_state, name="index-page"),
    path('region/<country_name>/<state_name>/<dict_name>', views.list_of_region_state_dict, name="index-page"),
    path('region/<country_name>/<state_name>/<dict_name>/<place_name>/pincode-or-zipcode', views.list_of_region_state_dict_pin_det, name="index-page"),
    path('searchpin/<pincode>', views.search_pincode, name="index-page"),
    path('sitemap.xml',views.sitemap, name="Sitemap Index")

     
]