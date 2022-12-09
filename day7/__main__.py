from dataclasses import dataclass
import sys
from util.run_util import runPart
from typing import Callable, Union

@dataclass
class File:
  name: str
  size: int
  
  def getSize(self) -> int:
    return self.size

@dataclass
class Dir:
  name: str
  parent: "Dir"
  children: dict[Union["Dir", File]]

  def getSize(self) -> int:
    return sum(child.getSize() for child in self.children.values())

def printFs(dir: Dir, depth=0):
  margin = " " * depth
  print(f"{margin}{dir.name} ({dir.getSize()})")
  for child in dir.children.values():
    if isinstance(child, File):
      print(f"{margin} {child.name} ({child.getSize()})")
    else:
      printFs(child, depth+1)
    
def doForEachDir(dir: Dir, fn: Callable[[Dir], None]):
  fn(dir)
  for child in dir.children.values():
    if isinstance(child, Dir):
      doForEachDir(child, fn)

TOP_DIR = "/"

def nextOrNone(iter) -> Union[str, None]:
  value = next(iter, None)
  if value == None:
    return value
  return value.rstrip()

def parseData(iterator):
  topDir = Dir(TOP_DIR, None, {})
  currDir = topDir
  text = nextOrNone(iterator)
  while text != None:
    tokens = text.split(" ")[1:]
    match tokens[0]:
      case "cd":
        match tokens[1]:                
          case "/":
            currDir = topDir
          case "..":                  
            if currDir.parent == None:
              raise Exception(f"No parent to navigate to! ({currDir.name})")
            currDir = currDir.parent
          case name:
            currDir = currDir.children.get(name)
        text = nextOrNone(iterator)
      case "ls":
        text = nextOrNone(iterator)
        while text != None and text[0] != "$":
          tokens = text.split(" ")
          name = tokens[1]
          match tokens[0]:
            case "dir":
              currDir.children[name] = Dir(name, currDir, {})
            case size:
              currDir.children[name] = File(name, int(size))
          text = nextOrNone(iterator)
  return topDir

def part1(filename):
  rootDir = parseData(iter(open(filename)))
  smallDirs = []
  doForEachDir(
    rootDir,
    lambda dir: smallDirs.append(dir.getSize()) if dir.getSize() <= 100000 else None
  )
  return f"Small dir total is {sum(smallDirs)}"

def part2(filename):
  diskSpace = 70000000
  rootDir = parseData(iter(open(filename)))
  neededSpace = 30000000 - (diskSpace - rootDir.getSize())

  print(neededSpace)

  bigDirs: list[Dir] = []
  doForEachDir(
    rootDir,
    lambda dir: bigDirs.append(dir) if dir.getSize() >= neededSpace else None
  )

  smallest = min(bigDirs, key=lambda dir: dir.getSize())

  return f"For needed size {neededSpace}, smallest dir to delete is {smallest.name} at {smallest.getSize()}"

if __name__ == "__main__":
  runPart(sys.argv, part1, part2)
