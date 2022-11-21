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

errors = 0
successes = 0
compiler_path = sys.argv[1]
interpreter_path = None
timeout = 5

# load supported extensions
extensions = []
if os.path.exists("extensions"):
	extensions = open("extensions").read().split()

if len(sys.argv) < 3:
	err("Please supply as second argument of test program path of your interpreter")
	note("Skipping interpreter tests")
	errors += 1
else:
	interpreter_path = sys.argv[2]



def run_test(path, files, name):
	if "name" not in files:
		test(name)
	else:
		test(open(path + "name").read().strip())
	is_ok = True
	proc = Popen([compiler_path], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	ret_code = None
	err_out = None
	try:
		out,err_out = proc.communicate(str.encode(open(path+"prog").read()), timeout=timeout)
		ret_code_comp = proc.returncode
		ret_code = ret_code_comp
		if "out" in files and interpreter_path is not None:
			expected_out = open(path+"out").read()
			# store current out to temp
			temp_out = open("temp_out","w")
			temp_out.write(out.decode("utf-8"))
			temp_out.close()
			proc = Popen([interpreter_path, "temp_out"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
			in_text = ""
			if "in" in files:
				in_text = open(path+"in").read().encode("utf-8")
			out_int,err_out_int = proc.communicate(in_text, timeout=timeout)
			ret_code_int = proc.returncode
			ret_code = ret_code or ret_code_int
			if out_int.decode("utf-8") != expected_out:
				err(f"Wrong output found {out_int.decode('utf-8')}, but expected {expected_out}")
				print(err_out_int.decode('utf-8'))
				print("INTERPRETER STDERR output:")
				is_ok = False
	except TimeoutExpired:
		err("Timeout expired")
		proc.kill()
		is_ok = False
	if "ret" in files and ret_code is not None:
		expected_ret = [*map(int,open(path+"ret").read().split("|"))]
		if ret_code not in expected_ret:
			err(f"Wrong error code found {ret_code}, but expected {' or '.join(map(str,expected_ret))}")
			is_ok = False
	if is_ok:
		succ("TEST SUCCESS")
	else:
		if err_out is not None:
			print("STDERR output:")
			print(err_out.decode("utf-8") )
		err("TEST FAILURE")
	return is_ok

is_ok = True
for root, dirs, files in os.walk("./tests"):
	path = root.split(os.sep)[2:]
	if path==[]:continue
	if "ext" in files:
		ext = open(root + "/ext").read().strip()
		if ext not in extensions:
			continue
	if "prog" in files:
		if not run_test(root + "/", files, path[-1]):
			is_ok = False
			errors += 1
		else:
			successes += 1
	else:
		print(Fore.YELLOW + "---"*(len(path)-1)+"> "+Fore.WHITE+path[-1])

print(f"Tests finished with {Fore.RED}{errors} errors{Fore.WHITE} and {Fore.GREEN}{successes} successes{Fore.WHITE}")
if errors == 0:
	print(Fore.GREEN + "WELL DONE!" + Fore.WHITE)

if not is_ok:
	sys.exit(1)
