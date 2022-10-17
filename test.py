#!/usr/bin/python3
import os
import sys
from subprocess import *
import getopt
try:
	from colorama import Fore
except:
	class Fore:
		RED="\x1b[31m"
		WHITE="\x1b[37m"
		CYAN="\x1b[36m"
		GREEN="\x1b[32m"
		BLUE="\x1b[34m"
		YELLOW="\x1b[36m"

def test(text):
	print("[TEST] " + text)

def err(text):
	print("[" + Fore.RED + "ERR" + Fore.WHITE + "] " + text)

def note(text):
	print("[ " + Fore.CYAN + "*" + Fore.WHITE + " ] " + text)

def succ(text):
	print("[" + Fore.GREEN + "OK" + Fore.WHITE + " ] " + text);

if len(sys.argv) < 2:
	err("Please supply as first argument of test program path of your compiler")
	exit()

compiler_path = sys.argv[1]
interpreter_path = ""



def run_test(path, files):
	is_ok = True
	proc = Popen([compiler_path], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	out,err_out = proc.communicate(str.encode(open(path+"prog").read()))
	ret_code = proc.returncode
	if "ret" in files:
		expected_ret = [*map(int,open(path+"ret").read().split("|"))]
		if ret_code not in expected_ret:
			err(f"Wrong error code found {ret_code}, but expected {' or '.join(map(str,expected_ret))}")
			is_ok = False
	if is_ok:
		succ("TEST SUCCESS")
	else:
		print("STDERR output:")
		print(err_out.decode("utf-8") )
		err("TEST FAILURE")
	return is_ok

for root, dirs, files in os.walk("./tests"):
	path = root.split(os.sep)[2:]
	if path==[]:continue
	if "prog" in files:
		test(path[-1])
		run_test(root + "/", files)
	else:
		print(Fore.YELLOW + "---"*(len(path)-1)+"> "+Fore.WHITE+path[-1])
	
