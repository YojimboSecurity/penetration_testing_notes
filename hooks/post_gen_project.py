import os
from pathlib import Path

path = Path(".")

def walk_path(path: Path):
    for i in path.iterdir():
        if i.is_dir:
            walk_path(i)
        if i.name == "README.txt":
            os.remove(i.absolute())
               
walk_path(path)
