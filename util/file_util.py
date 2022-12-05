import pathlib
import __main__
from typing import Callable, Any

def rfile(filename):
  return pathlib.Path(__main__.__file__).parent / filename

def forEachInput(filename, forEach: Callable[[str], None]):
  with open(filename) as file:
    for line in file:
      forEach(line.rstrip())

def mapEachInput(filename, mapFn: Callable[[str], Any]):
  with open(filename) as file:
    lines = []
    for line in file:
      lines.append(mapFn(line.rstrip()))
    return lines
