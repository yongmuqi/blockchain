import pip
from subprocess import call
from importlib import metadata as importlib_metadata
# 上一条语句在低版本中可能要改成 import importlib_metadata
for dist in importlib_metadata.distributions():
    print("Updating for:", dist.metadata["Name"])  # 看进度用，非必需
    call("pip install -U " + dist.metadata["Name"], shell=True)