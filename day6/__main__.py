import sys
from util.file_util import getCleanedInput
from util.run_util import runPart

def isDistinct(string: str):
  for i, x in enumerate(string):
    for j, y in enumerate(string):
      if i == j: # ignore same index
        continue
      if y == x:
        return False
  return True

def findFirstDistinct(data: str, size: int):
  marker: int = None
  for i in range(size, len(data)):
    slice = data[i-size:i]
    if isDistinct(slice):
      marker = i
      break
  return marker

def part1(filename):
  data = getCleanedInput(filename)[0]
  return f"First marker is at character {findFirstDistinct(data, 4)}"

def part2(filename):
  data = getCleanedInput(filename)[0]
  return f"First marker is at character {findFirstDistinct(data, 14)}"

if __name__ == "__main__":
  runPart(sys.argv, part1, part2)
