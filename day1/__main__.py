import sys
from util.file_util import mapEachInput
from util.run_util import runPart

def sumElfCalories(snacks):
  caloriesPerElf = []
  while ( snacks.count(None) > 0 ):
    idx = snacks.index(None)
    caloriesPerElf.append(sum(snacks[:idx]))
    snacks = snacks[idx+1:]
  return caloriesPerElf

def part1(filename):
  snacks = mapEachInput(filename, lambda line : int(line) if len(line) > 0 else None)
  caloriesPerElf = sumElfCalories(snacks)

  return f"Most calories is {max(caloriesPerElf)}"

def part2(filename):
  snacks = mapEachInput(filename, lambda line : int(line) if len(line) > 0 else None)
  
  caloriesPerElf = sumElfCalories(snacks)

  caloriesPerElf.sort(reverse=True)

  return f"Highest packers have a total of {sum(caloriesPerElf[:3])} calories"

if __name__ == "__main__":
  runPart(sys.argv, part1, part2)
