# coding: utf-8

from django.db.models import Q

from rql_filter.parser.parser import RQLParser
from rql_filter.parser.semantics import RQLSemantics


parser = RQLParser(semantics=RQLSemantics(), whitespace='')


def assert_query(rql, qstr):
    ast = parser.parse(rql)
    assert isinstance(ast, Q)
    assert ast.__str__() == qstr


def test_fiql_operators():
    assert_query(
        "field==value",
        "(AND: (u'field', u'value'))"
    )
    assert_query(
        "field!=value",
        "(NOT (AND: (u'field', u'value')))"
    )
    assert_query(
        "field=le=value",
        "(AND: (u'field__lte', u'value'))"
    )
    assert_query(
        "field=lt=value",
        "(AND: (u'field__lt', u'value'))"
    )
    assert_query(
        "field=ge=value",
        "(AND: (u'field__gte', u'value'))"
    )
    assert_query(
        "field=gt=value",
        "(AND: (u'field__gt', u'value'))"
    )
    assert_query(
        "field=in=value",
        "(AND: (u'field__in', u'value'))"
    )
    assert_query(
        "field=out=value",
        "(NOT (AND: (u'field__in', u'value')))"
    )


def test_rsql_operators():
    assert_query(
        "field<=value",
        "(AND: (u'field__lte', u'value'))"
    )
    assert_query(
        "field<value",
        "(AND: (u'field__lt', u'value'))"
    )
    assert_query(
        "field>=value",
        "(AND: (u'field__gte', u'value'))"
    )
    assert_query(
        "field>value",
        "(AND: (u'field__gt', u'value'))"
    )


def test_string_values():
    assert_query(
        "field=='single < quoted > with = \"special\" ! chars'",
        "(AND: (u'field', u'single < quoted > with = \"special\" ! chars'))"
    )
    assert_query(
        "field==\"double < quoted > with = 'special' ! chars\"",
        "(AND: (u'field', u\"double < quoted > with = 'special' ! chars\"))"
    )


def test_in_out():
    assert_query(
        "field=in=(value1,value2,value3)",
        "(AND: (u'field__in', [u'value1', u'value2', u'value3']))"
    )
    assert_query(
        "field=out=(value1,value2,value3)",
        "(NOT (AND: (u'field__in', [u'value1', u'value2', u'value3'])))"
    )


def test_and():
    assert_query(
        "field1==foo;field2==bar;field3==baz",
        "(AND: (u'field1', u'foo'), (u'field2', u'bar'), (u'field3', u'baz'))"
    )


def test_or():
    assert_query(
        "field1==foo,field2==bar,field3==baz",
        "(OR: (u'field1', u'foo'), (u'field2', u'bar'), (u'field3', u'baz'))"
    )


def test_priority():
    assert_query(
        "field1==foo,field2==bar;field3==baz",
        "(OR: (u'field1', u'foo'), (AND: (u'field2', u'bar'), (u'field3', u'baz')))"  # noqa
    )

    assert_query(
        "field1==foo;field2==bar,field3==baz",
        "(OR: (AND: (u'field1', u'foo'), (u'field2', u'bar')), (u'field3', u'baz'))"  # noqa
    )


def test_grouping():
    assert_query(
        "(field==value)",
        "(AND: (u'field', u'value'))"
    )
    assert_query(
        "((((field==value))))",
        "(AND: (u'field', u'value'))"
    )
    assert_query(
        "(field1==foo,field2==bar);field3==baz",
        "(AND: (OR: (u'field1', u'foo'), (u'field2', u'bar')), (u'field3', u'baz'))"  # noqa
    )
    assert_query(
        "field1==foo;(field2==bar,field3==baz)",
        "(AND: (u'field1', u'foo'), (OR: (u'field2', u'bar'), (u'field3', u'baz')))"  # noqa
    )
    assert_query(
        "(field1==foo;(field2==bar;(field3==baz;(field4==bang))))",
        "(AND: (u'field1', u'foo'), (u'field2', u'bar'), (u'field3', u'baz'), (u'field4', u'bang'))"  # noqa
    )
    assert_query(
        "(field1==foo,(field2==bar;(field3==baz,(field4==bang))))",
        "(OR: (u'field1', u'foo'), (AND: (u'field2', u'bar'), (OR: (u'field3', u'baz'), (u'field4', u'bang'))))"  # noqa
    )
