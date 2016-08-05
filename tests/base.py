# coding: utf-8


class RQLTestMixin(object):
    def do_rql_query(self, rql):
        raise NotImplementedError()

    def assert_rql_result(self, rql, expected_names):
        names = sorted([i['name'] for i in self.do_rql_query(rql)])
        assert ', '.join(names) == ', '.join(sorted(expected_names))

    def test_no_filter(self):
        self.assert_rql_result('', ['foo', 'bar', 'baz'])

    def test_eq(self):
        self.assert_rql_result('name==foo', ['foo'])

    def test_ne(self):
        self.assert_rql_result('name!=foo', ['bar', 'baz'])

    def test_in(self):
        self.assert_rql_result('name=in=(bar,baz)', ['bar', 'baz'])

    def test_out(self):
        self.assert_rql_result('name=out=(bar,baz)', ['foo'])

    def test_lt(self):
        self.assert_rql_result('number=lt=100', ['baz'])
        self.assert_rql_result('number<100', ['baz'])

    def test_lte(self):
        self.assert_rql_result('number=le=100', ['foo', 'baz'])
        self.assert_rql_result('number<=100', ['foo', 'baz'])

    def test_gt(self):
        self.assert_rql_result('number=gt=100', ['bar'])
        self.assert_rql_result('number>100', ['bar'])

    def test_gte(self):
        self.assert_rql_result('number=ge=100', ['foo', 'bar'])
        self.assert_rql_result('number>=100', ['foo', 'bar'])

    def test_and(self):
        self.assert_rql_result('name==foo,number>=100', ['foo'])
        self.assert_rql_result('name==foo,number>=200', [])

    def test_or(self):
        self.assert_rql_result('name==foo;number>=100', ['foo', 'bar'])
        self.assert_rql_result('name==foo;number>200', ['foo'])

    def test_relation(self):
        self.assert_rql_result('parent__name==foo-parent', ['foo', 'bar'])
