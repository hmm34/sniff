# Common utilities

import sys
from lxml import etree

def inputtree():
    string = ""
    data = sys.stdin.readlines()
    for i in range(0, len(data)):
        string += data[i]

    tree = etree.fromstring(string)
    return tree
