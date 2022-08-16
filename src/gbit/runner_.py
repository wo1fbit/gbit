#!/usr/bin/env python3

from os import path, listdir
import sys
from importlib import import_module
from termcolor import colored

def run():
	if len(sys.argv) != 2:
		print("Binary Missing")
		print("--------------")
		print("run: gbit [binary]")
		print("example: gbit less")
		sys.exit(0)

	gtfobin = sys.argv[1].lower()
	if gtfobin in ["var", 'var.py', '__init__', '__init__.py', 'runner_.py', 'runner_']:
		sys.exit()

	dir_path = path.dirname(path.realpath(__file__))+"/bin"
	binaries = listdir(dir_path)

	if gtfobin+".py" not in binaries:
		sys.exit()
	
	sys.path.insert(0, dir_path)
	module_s = import_module(f"{gtfobin}")
	print(module_s.gtfobin)

if __name__ == "__main__":
    run()