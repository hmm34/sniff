# Input: C++ Source code in XML
# Output: Function names with primitive parameters > n

import argparse
import util
from lxml import etree

parser = util.parser("threshold primitive parameter count for methods")
n = parser.parse_args().n

tree = util.inputtree()

predicate = '[count(src:parameter_list/src:parameter) > ' + `n` + ' ]'
query = '//src:function_decl' + predicate + ' | //src:constructor_decl' + predicate

r = tree.xpath(query,
    namespaces={'src': 'http://www.sdml.info/srcML/src',
                'cpp': 'http://www.sdml.info/srcML/cpp'})

for node in r:
    p = node.getparent()
    while p.getparent().getparent() is not None:
        p = p.getparent()

    info = p.get('filename')

    s = node.xpath('./src:name/text()',
        namespaces={'src': 'http://www.sdml.info/srcML/src',
                    'cpp': 'http://www.sdml.info/srcML/cpp'})
    info += ": " + s[0]
    print(info)
