# django-rql-filter

[![Build Status](https://travis-ci.org/njoyard/django-rql-filter.svg?branch=master)](https://travis-ci.org/njoyard/django-rql-filter)

This app implements a RQL/RSQL/FIQL filter backend for
[django-rest-framework](http://www.django-rest-framework.org) and enables
passing arbitrary conditional expressions to filter 

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

## Query syntax

A query is made using a combination of field comparisons.  Comparisons are
composed by a field name, an operator and a value.

| Operator    | Meaning                  | Examples               |
|:-----------:|--------------------------|------------------------|
| `==`        | Equal to                 | `name==bob`            |
| `!=`        | Not equal to             | `name!=bob`            |
| `<` `=lt=`  | Less than                | `age<30`  `age=lt=30`  |
| `<=` `=le=` | Less than or equal to    | `age<=30`  `age=le=30` |
| `>` `=gt=`  | Greater than             | `age<30`  `age=lt=30`  |
| `>=` `=ge=` | Greater than or equal to | `age<=30`  `age=le=30` |
| `=in=`      | Belongs to set           | `name=in=(bob,kate)`   |
| `=out=`     | Does not belong to set   | `name=out=(bob,kate)`  |

Values must be quoted with single or double quotes when they include special
characters or spaces: `name="bob katz"`.

Comparisons may be combined using `;` for a logical AND, and `,` for a logical
OR: `name="bob";age>=30`.  AND has priority over OR; grouping is available using
parentheses: `name="bob";(age>=30,age<3)`.

**Note:** RQL/RSQL/FIQL support is still incomplete, it will be enhanced over
time.

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
