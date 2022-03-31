from typing import Iterable, Iterator
from pytest import raises
from iterable_serialization.serialization import deserialize_iterable


def iterables_are_equal(val: Iterable, expect: Iterable) -> bool:
  assert isinstance(val, Iterable)
  assert isinstance(expect, Iterable)
  val_iterator = iter(val)
  expect_iterator = iter(expect)
  for v1 in val_iterator:
    try:
      v2 = next(expect_iterator)
    except StopIteration:
      return False
    if v1 != v2:
      return False
  try:
    next(expect_iterator)
  except StopIteration:
    return True
  return False


def test_component_aXbbXX__X__a_bb_X():
  result = deserialize_iterable("aXbbXX", "X")
  assert iterables_are_equal(result, ("a", "bb", "X"))


def test_empty__X__returns_empty():
  result = deserialize_iterable("", "X")
  assert iterables_are_equal(result, ())


def test_empty__empty__returns_empty():
  result = deserialize_iterable("", "")
  assert iterables_are_equal(result, ())


def test_a__empty__returns_a():
  result = deserialize_iterable("a", "")
  assert iterables_are_equal(result, ("a",))


def test_a__X__returns_a():
  result = deserialize_iterable("a", "X")
  assert iterables_are_equal(result, ("a",))


def test_aa__empty__returns_a_a():
  result = deserialize_iterable("aa", "")
  assert iterables_are_equal(result, ("a", "a"))


def test_aa__X__returns_aa():
  result = deserialize_iterable("aa", "X")
  assert iterables_are_equal(result, ("aa",))


def test_aXa__X__returns_a_a():
  result = deserialize_iterable("aXa", "X")
  assert iterables_are_equal(result, ("a", "a"))


def test_aaa__empty__returns_a_a_a():
  result = deserialize_iterable("aaa", "")
  assert iterables_are_equal(result, ("a", "a", "a"))


def test_aaa__X__returns_aaa():
  result = deserialize_iterable("aaa", "X")
  assert iterables_are_equal(result, ("aaa",))


def test_aXbXc__X__returns_a_b_c():
  result = deserialize_iterable("aXbXc", "X")
  assert iterables_are_equal(result, ("a", "b", "c"))


def test_aaXbb__X__returns_aa_bb():
  result = deserialize_iterable("aaXbb", "X")
  assert iterables_are_equal(result, ("aa", "bb"))


def test_aaXbbXcc__X__returns_aa_bb_cc():
  result = deserialize_iterable("aaXbbXcc", "X")
  assert iterables_are_equal(result, ("aa", "bb", "cc"))


def test_X__X__returns_X():
  result = deserialize_iterable("X", "X")
  assert iterables_are_equal(result, ("X",))


def test_XXX__X__returns_X_X():
  result = deserialize_iterable("XXX", "X")
  assert iterables_are_equal(result, ("X", "X"))


def test_XXa__X__returns_X_a():
  result = deserialize_iterable("XXa", "X")
  assert iterables_are_equal(result, ("X", "a"))


def test_aXX__X__returns_a_X():
  result = deserialize_iterable("aXX", "X")
  assert iterables_are_equal(result, ("a", "X"))
