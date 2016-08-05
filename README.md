# django-rql-filter

[![Build Status](https://travis-ci.org/njoyard/django-rql-filter.svg?branch=master)](https://travis-ci.org/njoyard/django-rql-filter)

This app implements a RQL/RSQL/FIQL filter backend for [django-rest-framework](http://www.django-rest-framework.org) and enables passing arbitrary conditional expressions to filter 

## Installation

```sh
pip install django-rql-filter
```

## Usage

Add `rql_filter` to your project `INSTALLED_APPS`.

Add the `RQLFilterBackend` to your viewset `filter_backends`:

```python
from rql_filter.backend import RQLFilterBackend

class ThingyViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (
        ...
        RQLFilterBackend,
        ...
    )
```

You may now pass a RQL/RSQL/FIQL query to API URLs using the `q` querystring
parameter:

```sh
curl http://my.app/api/thingies/?format=json&q=name==bob;age=gt=30
```

## Configuration

`RQL_FILTER_QUERY_PARAM` sets the querystring parameter name to use; it defaults
to `'q'`.

## Using without rest-framework

You may use the backend manually outside a rest-framework viewset:

```python
from rql_filter.backend import RQLFilterBackend

# May be reused any number of times
backend = RQLFilterBackend()

# Fake request object
class FakeRQLRequest:
    def __init__(self, q):
        self.GET = {'q': q}

qs = Thingy.objects.all()
filtered_qs = backend.filter_queryset(
    FakeRQLRequest('name==bob;age=gt=30'),
    qs,
    None
)
```

## Testing

Install testing dependencies:

```sh
pip install -e .[testing]
```

Run tests:

```sh
py.test
```
