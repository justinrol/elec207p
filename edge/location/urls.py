from django.conf.urls import url, include
from django.contrib import admin
from location.views import *


urlpatterns = [
    url(r'^$', test),

    url(r'^weather', get_weather)
]
