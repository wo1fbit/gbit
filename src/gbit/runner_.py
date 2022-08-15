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

	gtfobin = sys.argv[1]
	dir_path = path.dirname(path.realpath(__file__)) # get the path to the current directory
	binaries = listdir(dir_path) # get the modules

	if gtfobin.lower()+".py" not in binaries: # check if the requested binary is in the modules
		print(f"{gtfobin} yet to be added.")
		sys.exit(0)
	
	sys.path.insert(0, dir_path)
	module_s = import_module(f"{gtfobin}") # load the module
	print(module_s.gtfobin)

if __name__ == "__main__":
    run()