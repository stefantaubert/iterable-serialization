from typing import Generator, Iterable

def can_serialize_iterable(iterable: Iterable[str], split_symbol: str) -> bool:
  for symbol in iterable:
    if split_symbol in symbol and symbol != split_symbol:
      return False
  return True


def serialize_iterable(iterable: Iterable[str], split_symbol: str) -> str:
  if not isinstance(iterable, Iterable):
    raise ValueError("No iterable was passed!")
  assert len(split_symbol) == 1
  text = split_symbol.join(iterable)
  return text


def can_deserialize_iterable(serialized_iterable: str, split_symbol: str) -> bool:
  no_of_subsequent_split_symbols = 1
  last_char_was_non_split_symbol = False
  for char in serialized_iterable:
    if char == split_symbol:
      no_of_subsequent_split_symbols += 1
      last_char_was_non_split_symbol = False
    else:
      if no_of_subsequent_split_symbols % 2 == 0 and not last_char_was_non_split_symbol:
        return False
      no_of_subsequent_split_symbols = 0
      last_char_was_non_split_symbol = True
  if no_of_subsequent_split_symbols % 2 == 0:
    return True
  return False


def deserialize_iterable(serialized_iterable: str, split_symbol: str) -> Generator[str, None, None]:
  #assert can_deserialize(text, split_symbol)
  assert len(split_symbol) == 1
  symbol = ""
  yield_subsequent_split_symbol = None
  for char in serialized_iterable:
    if char == split_symbol:
      if symbol == "":
        if yield_subsequent_split_symbol is None:
          yield char
          yield_subsequent_split_symbol = False
        elif yield_subsequent_split_symbol:
          yield char
          yield_subsequent_split_symbol = False
        else:
          yield_subsequent_split_symbol = True
      else:
        yield symbol
        symbol = ""
        yield_subsequent_split_symbol = True
    else:
      symbol += char
  if symbol != "":
    yield symbol
