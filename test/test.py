import subprocess

def launch_test(program):
	input = ["cat", "input.xml"]
	pin = subprocess.Popen(input, stdout=subprocess.PIPE)
	pout = subprocess.Popen(program, stdin=pin.stdout, stdout=subprocess.PIPE)
	return pout.communicate()


input = ["cat", "input.xml"]

# test count-comments
prog = ["python", "../count-comments.py"]
out, err = launch_test(prog)
assert (out.rstrip('\n') == "7")

# test class with 5 or more member variables
prog = ["python", "../long-class.py", "5"]
out, err = launch_test(prog)
assert(out.rstrip('\n') == "../../testdata/project/circle.h: Circle")

# test method with 5 or more lines
prog = ["python", "../long-method.py", "5"]
out, err = launch_test(prog)
assert(out.rstrip('\n') == "../../testdata/project/circle.cpp: Circle")
