# coding: utf-8

from django import test

from rql_filter.backend import RQLFilterBackend

from .base import RQLTestMixin
from .models import Child


class FakeRequest:
    def __init__(self, q):
        self.GET = {'q': q}


class TestQueries(RQLTestMixin, test.TestCase):
    backend = RQLFilterBackend()

    def do_rql_query(self, rql):
        return self.backend.filter_queryset(
            FakeRequest(rql),
            Child.objects.all(),
            None
        ).values('name')
