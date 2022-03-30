from enum import IntEnum
from typing import Tuple
from iterable_serialization.str_serialization import (can_deserialize_symbols,
                                                      can_serialize_symbols,
                                                      deserialize_symbols,
                                                      serialize_symbols)


DEFAULT_SPACED_SEP = " "


class StringFormat2(IntEnum):
  DEFAULT = 0
  # rename to separated
  SPACED = 1

  def convert_string_to_symbols(self, string: str, sep: str = DEFAULT_SPACED_SEP) -> Tuple[str, ...]:
    return convert_string_to_symbols(string, self, sep)

  def convert_symbols_to_string(self, symbols: Tuple[str, ...], sep: str = DEFAULT_SPACED_SEP) -> str:
    return convert_symbols_to_string(symbols, self, sep)

  def can_convert_string_to_symbols(self, string: str, sep: str = DEFAULT_SPACED_SEP) -> bool:
    return can_convert_string_to_symbols(string, self, sep)

  def can_convert_symbols_to_string(self, symbols: Tuple[str, ...], sep: str = DEFAULT_SPACED_SEP) -> bool:
    return can_convert_symbols_to_string(symbols, self, sep)


def can_convert_string_to_symbols(string: str, string_format: StringFormat2, sep: str) -> bool:
  if string_format == StringFormat2.SPACED:
    return can_deserialize_symbols(string, sep)
  if string_format == StringFormat2.DEFAULT:
    return True
  assert False


def can_convert_symbols_to_string(symbols: Tuple[str, ...], string_format: StringFormat2, sep: str) -> bool:
  if string_format == StringFormat2.SPACED:
    return can_serialize_symbols(symbols, sep)
  if string_format == StringFormat2.DEFAULT:
    return True
  assert False


def get_other_format(string_format: StringFormat2) -> StringFormat2:
  if string_format == StringFormat2.SPACED:
    return StringFormat2.DEFAULT
  if string_format == StringFormat2.DEFAULT:
    return StringFormat2.SPACED
  assert False


def convert_string_to_symbols(string: str, string_format: StringFormat2, sep: str) -> Tuple[str, ...]:
  assert isinstance(string, str)
  assert isinstance(string_format, StringFormat2)
  if string_format == StringFormat2.SPACED:
    return tuple(deserialize_symbols(string, sep))
  if string_format == StringFormat2.DEFAULT:
    return convert_text_string_to_symbols(string)
  assert False


def convert_symbols_to_string(symbols: Tuple[str, ...], string_format: StringFormat2, sep: str) -> str:
  assert isinstance(symbols, tuple)
  assert isinstance(string_format, StringFormat2)
  if string_format == StringFormat2.SPACED:
    return serialize_symbols(symbols, sep)
  if string_format == StringFormat2.DEFAULT:
    return convert_symbols_to_text_string(symbols)
  assert False


def convert_text_string_to_symbols(text_string: str) -> Tuple[str, ...]:
  result = tuple(text_string)
  return result


def convert_symbols_to_text_string(symbols: Tuple[str, ...]) -> str:
  result = "".join(symbols)
  return result
