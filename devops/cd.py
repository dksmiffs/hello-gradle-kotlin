# guidance:  https://stackoverflow.com/a/24176022
from contextlib import contextmanager
import os

@contextmanager
def cd(newdir):
  prevdir = os.getcwd()
  os.chdir(os.path.expanduser(newdir))
  try:
    yield
  finally:
    os.chdir(prevdir)

