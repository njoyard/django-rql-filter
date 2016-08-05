# coding: utf-8

import json
import urllib

from django import test

from .base import RQLTestMixin


class TestRestFramework(RQLTestMixin, test.TestCase):

    def do_rql_query(self, rql):
        url = '/api/children/?format=json'
        if rql:
            url = '%s&q=%s' % (url, urllib.quote(rql))

        with self.assertNumQueries(1):
            return json.loads(test.client.Client().get(url).content)
