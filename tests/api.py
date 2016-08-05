# coding: utf-8

from rest_framework import viewsets

from rql_filter.backend import RQLFilterBackend

from .serializers import ChildSerializer
from .models import Child


class ChildViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Child.objects.all()
    filter_backends = (RQLFilterBackend,)
    serializer_class = ChildSerializer
