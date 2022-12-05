import sys
from util.run_util import runPart
from util.file_util import mapEachInput

def mapCode(value):
  match(value):
    case "A" | "X": # rock
      return 0
    case "B" | "Y": # paper
      return 1
    case "C" | "Z": # scissors
      return 2

def parseInput(filename):
  return mapEachInput(filename, lambda line: tuple(
    [ mapCode(choice) for choice in line.split(" ") ]
  ))

def calculateScore(opp, you):
  if opp == you: # draw
    return 3 + you + 1
  # If you are 1 less than opp, you are the choice which loses to him
  # i.e. rock (0) is 1 less than paper (1): loss
  if you == ((opp - 1) % 3): # loss
    return 0 + you + 1
  return you + 6 + 1 # win

def part1(filename):
  plays = parseInput(filename)
  score = 0

  for (opp, you) in plays:
    score += calculateScore(opp, you)

  return f"Your final score is {score}"

# Intent is defined as 0 for loss, 1 for tie, 2 for win
# Intent - 1 is the diff in your opponents choice to make you do that
# rock - 1 == scissors which means you will lose
def chooseHand(opp, intent):
  return (opp + intent - 1) % 3 

def part2(filename):
  plays = parseInput(filename)
  score = 0

  for (opp, intent) in plays:
    score += calculateScore(opp, chooseHand(opp, intent))

  return f"Your final score is {score}"

if __name__ == "__main__":
  runPart(sys.argv, part1, part2)
