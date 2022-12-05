import pathlib
import sys

def rfile(filename):
  return pathlib.Path(__file__).parent / filename

def forEachInput(filename, forEach):
  with open(filename) as file:
    for line in file:
      forEach(line.rstrip())

def mapEachInput(filename, mapFn):
  with open(filename) as file:
    lines = []
    for line in file:
      lines.append(mapFn(line.rstrip()))
    return lines

def getArgs(args):
  print(args)
  if len(args) < 2:
    raise Exception("Must give part # as first argument.")
  return (
    int(args[1]),
    args[2] if len(args) > 2 else None
  )

def pickFile(mode):
  return rfile('./test.txt' if mode == "test" else './input.txt')

def runPart(args, *partFns):
  print(partFns)
  (part, mode) = getArgs(args)
  print(part, mode)
  partFns[part-1](pickFile(mode))

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

  print(f"Most calories is {max(caloriesPerElf)}")

def part2(filename):
  snacks = mapEachInput(filename, lambda line : int(line) if len(line) > 0 else None)
  
  caloriesPerElf = sumElfCalories(snacks)

  caloriesPerElf.sort(reverse=True)

  print(caloriesPerElf[:3])

  print(f"Highest packers have a total of {sum(caloriesPerElf[:3])} calories")

runPart(sys.argv, part1, part2)
