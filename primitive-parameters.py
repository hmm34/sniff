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
    namespaces=util.srcml_ns())

for node in r:
    info = filename(node)

    s = node.xpath('./src:name/text()',
        namespaces=util.srcml_ns())
    info += ": " + s[0]
    print(info)
