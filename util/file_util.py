import pathlib
import __main__
from typing import Callable, TypeVar

T = TypeVar("T")

def rfile(filename):
  return pathlib.Path(__main__.__file__).parent / filename

def forEachInput(filename, forEach: Callable[[str], None]):
  with open(filename) as file:
    for line in file:
      forEach(line.rstrip())

def mapEachInput(filename, mapFn: Callable[[str], T]) -> list[T]:
  with open(filename) as file:
    lines = []
    for line in file:
      lines.append(mapFn(line.rstrip()))
    return lines

def getCleanedInput(filename):
  return mapEachInput(filename, lambda x: x)