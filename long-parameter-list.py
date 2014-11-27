# Input: Source code in XML
# Output: Functions matching a parameter list > n

import util
from lxml import etree

tree = util.inputtree()

n = 2
query = '//src:function[count(src:parameter_list/src:param) > ' + `n` + ' ]'
query +=' | '
query += '//src:constructor[count(src:parameter_list/src:param) > ' + `n` + ' ]'

r = tree.xpath(query,
    namespaces={'src': 'http://www.sdml.info/srcML/src',
                'cpp': 'http://www.sdml.info/srcML/cpp'})

for node in r:
    print(etree.tostring(node))
