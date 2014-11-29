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
expect = "project/circle.hpp: Circle\n"
expect += "std::string name;\n"
expect += "int area;\n"
expect += "int var1;\n"
expect += "int var2;\n"
expect += "int var3;\n"
expect += "int var4;\n"
expect += "int var5;\n"
expect += "int var6;\n"
expect += "int var7;\n"
expect += "int var8;\n"
expect += "int var9;\n"
expect += "int var10;\n"
expect += "int var11;\n"
expect += "int var12;\n"
expect += "int var13;"
launch_test(prog, expect)
