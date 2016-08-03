# coding: utf-8

from django import test

from rql_filter.backend import RQLFilterBackend

from .models import Child


class FakeRequest:
    def __init__(self, q):
        self.GET = {'q': q}


class TestQueries(test.TestCase):
    backend = RQLFilterBackend()

    def query_model(self, rql, expected_names):
        names = sorted([
            i['name'] for i in self.backend.filter_queryset(
                FakeRequest(rql),
                Child.objects.all(),
                None
            ).values('name')
        ])

        assert ', '.join(names) == ', '.join(sorted(expected_names))

    def test_no_filter(self):
        self.query_model('', ['foo', 'bar', 'baz'])

    def test_eq(self):
        self.query_model('name==foo', ['foo'])

    def test_ne(self):
        self.query_model('name!=foo', ['bar', 'baz'])

    def test_in(self):
        self.query_model('name=in=(bar,baz)', ['bar', 'baz'])

    def test_out(self):
        self.query_model('name=out=(bar,baz)', ['foo'])

    def test_lt(self):
        self.query_model('number=lt=100', ['baz'])
        self.query_model('number<100', ['baz'])

    def test_lte(self):
        self.query_model('number=le=100', ['foo', 'baz'])
        self.query_model('number<=100', ['foo', 'baz'])

    def test_gt(self):
        self.query_model('number=gt=100', ['bar'])
        self.query_model('number>100', ['bar'])

    def test_gte(self):
        self.query_model('number=ge=100', ['foo', 'bar'])
        self.query_model('number>=100', ['foo', 'bar'])

    def test_and(self):
        self.query_model('name==foo,number>=100', ['foo'])
        self.query_model('name==foo,number>=200', [])

    def test_or(self):
        self.query_model('name==foo;number>=100', ['foo', 'bar'])
        self.query_model('name==foo;number>200', ['foo'])
