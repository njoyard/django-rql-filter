# coding: utf-8

from django.conf import settings
from rest_framework.filters import BaseFilterBackend

from parser.parser import RQLParser
from parser.semantics import RQLSemantics


class RQLFilterBackend(BaseFilterBackend):
    """
    Filter that uses a RQL query.

    The RQL query is expected to be passed as a querystring parameter.
    The RQL_FILTER_QUERY_PARAM setting (which defaults to 'q') specifies the
    name of the querystring parameter used.
    """

    parser = RQLParser(semantics=RQLSemantics())
    query_param = getattr(settings, 'RQL_FILTER_QUERY_PARAM', 'q')

    def filter_queryset(self, request, queryset, view):
        qs = queryset

        if self.query_param in request.GET:
            if len(request.GET[self.query_param]):
                condition = self.parser.parse(request.GET[self.query_param])
                qs = qs.filter(condition)

        return qs
