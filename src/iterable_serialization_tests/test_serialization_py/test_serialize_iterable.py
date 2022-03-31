from pytest import raises
from iterable_serialization.serialization import serialize_iterable


def test_empty__X__returns_empty():
  result = serialize_iterable((), "X")
  assert result == ""


def test_empty__empty__returns_empty():
  result = serialize_iterable((), "")
  assert result == ""


def test_empty__None__returns_empty():
  result = serialize_iterable((), None)
  assert result == ""


def test_a__X__returns_a():
  result = serialize_iterable(("a",), "X")
  assert result == "a"


def test_a__empty__returns_a():
  result = serialize_iterable(("a",), "")
  assert result == "a"


def test_a__None__returns_a():
  result = serialize_iterable(("a",), None)
  assert result == "a"


def test_aa__X__returns_aa():
  result = serialize_iterable(("aa",), "X")
  assert result == "aa"


def test_aa__empty__returns_aa():
  result = serialize_iterable(("aa",), "")
  assert result == "aa"


def test_a_a__X_returns_aXa():
  result = serialize_iterable(("a", "a"), "X")
  assert result == "aXa"


def test_a_a__empty_returns_aa():
  result = serialize_iterable(("a", "a"), "")
  assert result == "aa"


def test_a_a_a__X__returns_aXaXa():
  result = serialize_iterable(("a", "a", "a"), "X")
  assert result == "aXaXa"


def test_a_a_a__empty__returns_aXaXa():
  result = serialize_iterable(("a", "a", "a"), "")
  assert result == "aaa"


def test_aa_aa__X__returns_aaXaa():
  result = serialize_iterable(("aa", "aa"), "X")
  assert result == "aaXaa"


def test_aa_aa__empty__returns_aaaa():
  result = serialize_iterable(("aa", "aa"), "")
  assert result == "aaaa"


def test_X_a__X__returns_XXa():
  result = serialize_iterable(("X", "a"), "X")
  assert result == "XXa"


def test_a_X__X__returns_aXX():
  result = serialize_iterable(("a", "X"), "X")
  assert result == "aXX"


def test_X__X__returns_X():
  result = serialize_iterable(("X"), "X")
  assert result == "X"


def test_X_X__X__returns_XXX():
  result = serialize_iterable(("X", "X"), "X")
  assert result == "XXX"


def test_X_X_X__X__returns_XXXXX():
  result = serialize_iterable(("X", "X", "X"), "X")
  assert result == "XXXXX"


def test_number__X__raises_value_error():
  with raises(ValueError):
    serialize_iterable((1,), "X")


def test_number__empty__raises_value_error():
  with raises(ValueError):
    serialize_iterable((1,), "")


def test_one_empty_entry__X__raises_value_error():
  with raises(ValueError):
    serialize_iterable(("",), "X")


def test_one_empty_entry__empty__raises_value_error():
  with raises(ValueError):
    serialize_iterable(("",), "")


def test_non_iterable__X__raises_value_error():
  with raises(ValueError):
    serialize_iterable(object(), "X")


def test_non_iterable__empty__raises_value_error():
  with raises(ValueError):
    serialize_iterable(object(), "")


def test_a__1__raises_value_error():
  with raises(ValueError):
    serialize_iterable(("a",), 1)


def test_a__XX__raises_value_error():
  with raises(ValueError):
    serialize_iterable(("a",), "XX")


def test_aX__X__raises_value_error():
  with raises(ValueError):
    serialize_iterable(("aX",), "X")
