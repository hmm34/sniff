# Input: Source code in XML
# Output: Function names matching a parameter list > n

import util
from lxml import etree

tree = util.inputtree()

n = 1
predicate = '[count(src:parameter_list/src:param) > ' + `n` + ' ]'
query = '//src:function' + predicate + ' | //src:constructor' + predicate

r = tree.xpath(query,
    namespaces={'src': 'http://www.sdml.info/srcML/src',
                'cpp': 'http://www.sdml.info/srcML/cpp'})

for node in r:
    s = node.xpath('(./src:name/src:name/text())[last()]',
        namespaces={'src': 'http://www.sdml.info/srcML/src',
                    'cpp': 'http://www.sdml.info/srcML/cpp'})
    print(s[0])
