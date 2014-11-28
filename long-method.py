# Input: Source code in XML
# Output: Function names whose contents exceed n lines

import util
from lxml import etree

tree = util.inputtree()

n = 200

r = tree.xpath('//src:function | //src:constructor',
    namespaces={'src': 'http://www.sdml.info/srcML/src',
                'cpp': 'http://www.sdml.info/srcML/cpp'})

for node in r:
	string = etree.tostring(node)
	if string.count('\n') > n:
		s = node.xpath('(./src:name/src:name/text())[last()]',
            namespaces={'src': 'http://www.sdml.info/srcML/src',
                        'cpp': 'http://www.sdml.info/srcML/cpp'})
		print(s[0])
