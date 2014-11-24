# Counts the number of line and block comments in a srcML file

import sys
import StringIO
from lxml import etree

string = ""
data = sys.stdin.readlines()
for i in range(0, len(data)):
	string += data[i]

tree = etree.fromstring(string)

r = tree.xpath('//src:comment',
	namespaces={'src': 'http://www.sdml.info/srcML/src',
			    'cpp': 'http://www.sdml.info/srcML/cpp'})

print(len(r))
