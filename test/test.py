import subprocess

def launch_test(program, expected_output):
	input = ["cat", "input.xml"]
	pin = subprocess.Popen(input, stdout=subprocess.PIPE)
	pout = subprocess.Popen(program, stdin=pin.stdout, stdout=subprocess.PIPE)
	out, err = pout.communicate()
	assert(out.rstrip('\n') == expected_output)

# test count-comments
prog = ["python", "../count-comments.py"]
expect = "7"
launch_test(prog, expect)

# test class with 5 or more member variables
prog = ["python", "../long-class.py", "5"]
expect = "project/circle.hpp: Circle"
launch_test(prog, expect)

# test method with 5 or more lines
prog = ["python", "../long-method.py", "5"]
expect = "project/circle.cpp: Circle"
launch_test(prog, expect)

# test method with 3 or more parameters
prog = ["python", "../long-parameter-list.py", "3"]
expect = "project/circle.hpp: reallyLongParameters"
launch_test(prog, expect)

# test classes with 3 or more primitive fields
prog = ["python", "../primitive-fields.py", "10"]
expect = "project/circle.hpp: Circle"
launch_test(prog, expect)

# test method with 3 or more primitive parameters
prog = ["python", "../primitive-parameters.py", "3"]
expect = "project/circle.hpp: reallyLongParameters"
launch_test(prog, expect)
