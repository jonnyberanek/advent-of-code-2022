from functools import reduce
import sys
from dataclasses import dataclass
from util.file_util import getCleanedInput
from util.run_util import runPart
from collections import deque

@dataclass
class Instruction:
  amount: int
  src: int
  dest: int

def parseCrateLayout(layoutData: list[str]) -> list[list[str]]:
  numRow = layoutData.pop()
  layoutData.reverse()
  stacks = []
  for i, char in enumerate(numRow):
    if not char.isdigit():
      continue
    stack = []
    for row in layoutData:
      if len(row) < i or row[i] == " ":
        break
      stack.append(row[i])
    stacks.append(stack)

  return stacks

def parseInstructions(instructionList: list[str]):
  return [ parseInstruction(instr) for instr in instructionList ]  

def parseInstruction(instruction: str):
  args = [ int(x) for x in instruction.split(" ") if x.isdigit() ]
  # -1 accounts for instructions being 1-indexed
  return Instruction(args[0], args[1]-1, args[2]-1)

def parseInput(input):
  sepIndex = input.index("")
  return (
    parseCrateLayout(input[:sepIndex]),
    parseInstructions(input[sepIndex+1:])
  )

# In-place operation, stacks is modified
def doInstructionSeq(stacks: list[list[str]], instr: Instruction):
  for _ in range(instr.amount):
    stacks[instr.dest].append(stacks[instr.src].pop())

# In-place operation, stacks is modified
def doInstructionStacked(stacks: list[list[str]], instr: Instruction):
  chunk = deque()
  for _ in range(instr.amount):
    chunk.appendleft(stacks[instr.src].pop())
  stacks[instr.dest] += chunk

def formatTopCrates(stacks):
  return reduce(lambda acc, curr: acc + curr[len(curr)-1], stacks, "")

def getTopCrates(data, moveFn):
  (stacks, instructions) = parseInput(data)
  
  for instr in instructions:
    moveFn(stacks, instr)
  
  return f"Top crates are {formatTopCrates(stacks)}"

def part1(filename):
  return getTopCrates(getCleanedInput(filename), doInstructionSeq)

def part2(filename):
  return getTopCrates(getCleanedInput(filename), doInstructionStacked)

if __name__ == "__main__":
  runPart(sys.argv, part1, part2)
