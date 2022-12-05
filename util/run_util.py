from util.file_util import rfile
from typing import Callable

def getArgs(args):
  if len(args) < 2:
    raise Exception("Must give part # as first argument.")
  return (
    int(args[1]),
    args[2] if len(args) > 2 else None
  )

def pickFile(mode):
  return rfile('./test.txt' if mode == "test" else './input.txt')

def runPart(args, *partFns: Callable[[str], str]) -> str:
  (part, mode) = getArgs(args)
  print(partFns[part-1](pickFile(mode)))