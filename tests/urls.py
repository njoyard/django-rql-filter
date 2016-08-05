# coding: utf-8

from django.conf.urls import include, url

from rest_framework import routers

from .api import ChildViewSet


router = routers.DefaultRouter()
router.register('children', ChildViewSet)

urlpatterns = [
    url('api/', include(router.urls)),
]
