# iterable-serialization

[![PyPI](https://img.shields.io/pypi/v/iterable-serialization.svg)](https://pypi.python.org/pypi/iterable-serialization)
[![PyPI](https://img.shields.io/pypi/pyversions/iterable-serialization.svg)](https://pypi.python.org/pypi/iterable-serialization)
[![MIT](https://img.shields.io/github/license/stefantaubert/iterable-serialization.svg)](LICENSE)

Serialization and deserialization of iterables with elements of type `str` from and to a string; similar to `str.join(...)`.

This package aims to be an improved version of:

```python
# serialization
>>> serialized = "|".join(("a", "b", "c"))
>>> serialized
'a|b|c'

# deserialization
>>> deserialized = serialized.split("|")
>>> deserialized
['a', 'b', 'c']
```

It makes it possible to serialize/deserialize an iterable with occurring symbols as separator:

```python
>>> from iterable_serialization import deserialize_iterable, serialize_iterable

# serialization
>>> serialized = serialize_iterable(("a", "b", "c"), "a")
>>> serialized
'aabac'

# deserialization
>>> deserialized = deserialize_iterable(serialized, "a")
>>> tuple(deserialized)
('a', 'b', 'c')
```

With the version above, it would result in a wrong deserialization result:

```python
# serialization
>>> serialized = "a".join(("a", "b", "c"))
>>> serialized
'aabac'

# deserialization
>>> deserialized = serialized.split("a")
>>> deserialized
['', '', 'b', 'c']
```

## Installation

```sh
pip install iterable-serialization
```

## Usage

```python
>>> from iterable_serialization import deserialize_iterable, serialize_iterable

# serialization
>>> serialized = serialize_iterable(("a", "b", "c"), "a")
>>> serialized
'aabac'

# deserialization
>>> deserialized = deserialize_iterable(serialized, "a")
>>> tuple(deserialized)
('a', 'b', 'c')
```
