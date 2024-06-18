import sys
from pathlib import Path

class PathFinder:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(PathFinder, cls).__new__(cls)
        return cls.instance
    
    @staticmethod
    def find_basedir() -> Path:
        sys_dirs = [Path(dir) for dir in sys.path if dir]
        
        