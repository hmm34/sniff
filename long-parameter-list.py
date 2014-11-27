# Input: Source code in XML
# Output: Functions matching a parameter list > n

import util

tree = util.inputtree()

r = tree.xpath('//src:function | //src:constructor',
    namespaces={'src': 'http://www.sdml.info/srcML/src',
                'cpp': 'http://www.sdml.info/srcML/cpp'})

for node in r:
    print(etree.tostring(node))