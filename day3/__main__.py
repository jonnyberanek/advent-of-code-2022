import sys
from util.file_util import getCleanedInput, mapEachInput
from util.run_util import runPart

ord_a = ord("a")
ord_A = ord("A")

def getPriority(item: str):
  if(item.isupper()):
    return ord(item) - ord_A + 27
  else:
    return ord(item) - ord_a + 1

def getSack(iter) -> tuple[str,str]:
  split = int(len(iter)/2)
  return (iter[:split], iter[split:])

def part1(filename):
  sepsacks = mapEachInput(filename, getSack)
  badItems = []
  for sack in sepsacks:
    for item in sack[0]:
      if item in sack[1]:
        badItems.append(item)
        break
  
  totalPriority = sum(getPriority(item) for item in badItems)
  return f"Total repack priority is {totalPriority}"

def findBadge(sacks, i):
  sameItems = (item for item in sacks[i+1] if item in sacks[i])
  for item in sameItems:
    if item in sacks[i+2]:
      return item


def part2(filename):
  sacks = getCleanedInput(filename)

  badges = []
  i = 0
  while (i < len(sacks)):
    badges.append(findBadge(sacks, i))
    i += 3

  totalPriority = sum(getPriority(item) for item in badges)
  return f"Total badge priority is {totalPriority}"

if __name__ == "__main__":
  runPart(sys.argv, part1, part2)
