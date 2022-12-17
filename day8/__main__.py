from functools import reduce
import sys
from util.file_util import mapEachInput
from util.run_util import runPart

def parseHeights(line: str):
  return [int(c) for c in line]

def isVisible(height: int, others: list[int]):
  for h in others:
    if h >= height:
      return False
  return True

def isBorder(value, length):
  return value == 0 or value == length-1

def getEdges(heights, x, y):
  row = heights[y]
  col = [r[x] for r in heights] 

  return [row[:x], row[x+1:], col[:y], col[y+1:]]

def part1(filename):
  heights = mapEachInput(filename, parseHeights)

  visible = 0 
  for y, targetRow in enumerate(heights):
    if isBorder(y, len(heights)):
      visible += len(heights)
      continue
    for x, targetTree in enumerate(targetRow):
      if isBorder(x, len(heights)):
        visible += 1
        continue

      edgeTrees = getEdges(heights, x, y)
      
      visibility = [isVisible(targetTree, trees) for trees in edgeTrees]
      if any(visibility):
        visible += 1

  return f"There are {visible} visible trees."

# others should be orders from closest to farthest
def getViewCount(target, others):
  for i, h in enumerate(others):
    if h >= target:
      return i+1
  return len(others)

def multiply(x, y):
  return x * y

def part2(filename):
  heights = mapEachInput(filename, parseHeights)

  highestScore = 0

  for y, targetRow in enumerate(heights):
    if isBorder(y, len(heights)):
      continue
    for x, targetTree in enumerate(targetRow):
      if isBorder(x, len(heights)):
        continue

      # left, right, top, bottom
      edgeTrees = getEdges(heights, x, y)
      edgeTrees[0].reverse()
      edgeTrees[2].reverse()
      
      score = reduce(
        multiply,
        (getViewCount(targetTree, trees) for trees in edgeTrees)
      )
      
      if score > highestScore:
        highestScore = score

  return f"Best scenic score possible is {highestScore}"

if __name__ == "__main__":
  runPart(sys.argv, part1, part2)
