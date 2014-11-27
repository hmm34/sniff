# Input: Source code in XML
# Output: Functions matching a parameter list > n

import sys
from lxml import etree

string = ""
data = sys.stdin.readlines()
for i in range(0, len(data)):
    string += data[i]

tree = etree.fromstring(string)

r = tree.xpath('//src:function | //src:constructor',
    namespaces={'src': 'http://www.sdml.info/srcML/src',
                'cpp': 'http://www.sdml.info/srcML/cpp'})

for node in r:
    print(etree.tostring(node))