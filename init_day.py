import __main__
from pathlib import Path
import sys

from util.file_util import rfile

if __name__ == "__main__":
  if len(sys.argv) < 2:
    raise Exception("Must provide number for day")
  
  dayNum = int(sys.argv[1])

  dirPath = Path(rfile(f"day{dayNum}"))
  
  dirPath.mkdir(exist_ok=True)

  (dirPath / "input.txt").touch()
  (dirPath / "test.txt").touch()
  
  mainPy = (dirPath / "__main__.py")
  mainPy.touch()
  mainPy.write_text(
    open(rfile("template.py")).read()
  )

  print(f"Day {dayNum} created successfully!")

  