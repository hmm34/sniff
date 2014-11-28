import subprocess

input = ["cat", "input.xml"]
prog = ["python", "../count-comments.py"]

pin = subprocess.Popen(input, stdout=subprocess.PIPE)
pout = subprocess.Popen(prog, stdin=pin.stdout, stdout=subprocess.PIPE)

out, err = pout.communicate()

assert (out.rstrip('\n') == "7")
