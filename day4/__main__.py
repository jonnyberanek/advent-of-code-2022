import sys
from util.file_util import mapEachInput
from util.run_util import runPart
from collections import namedtuple

Section = namedtuple("Section", "s e") 

def isIn(a,b):
  return (a.s >= b.s) and (a.e <= b.e)

def isOverlapping(a,b):
  return (a.e >= b.s and a.e <= b.e) or (b.e >= a.s and b.e <= a.e)

def parseInput(line):
  return tuple(Section(
        *(int(s) for s in assn.split("-"))
      ) for assn in line.split(",")
    )

def part1(filename):
  elfPairs = mapEachInput(filename, parseInput)

  overlaps = 0
  for pair in elfPairs:
    if isIn(pair[0], pair[1]) or isIn(pair[1], pair[0]):
      overlaps += 1
  
  return f"Number of full contains is {overlaps}"

def part2(filename):
  elfPairs = mapEachInput(filename, parseInput)
  
  overlaps = 0
  for pair in elfPairs:
    if isOverlapping(pair[1], pair[0]):
      overlaps += 1
  
  return f"Number of overlaps is {overlaps}"

if __name__ == "__main__":
  runPart(sys.argv, part1, part2)
