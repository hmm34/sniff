# Input: C++ Source code in XML
# Output: Function names with primitive parameters > n

import argparse
import util
from lxml import etree

parser = util.parser("threshold primitive parameter count for methods")
n = parser.parse_args().n

tree = util.inputtree()

predicate = '[count(src:parameter_list/src:parameter) > ' + `n` + ' ]'

types = util.primitives()
types_query = "[./src:decl/src:type/src:name[ "
for i in range(0, len(types)):
    types_query += ". = '" + types[i] + "' "
    if i != len(types) - 1:
        types_query += " or "
types_query += " ]]"

predicate = "[count(src:parameter_list/src:parameter" + types_query + ") > " + `n` + ' ]'
query = '//src:function_decl' + predicate + ' | //src:constructor_decl' + predicate

r = tree.xpath(query,
    namespaces=util.srcml_ns())

for node in r:
    #print("===========")
    #print(etree.tostring(node))
    info = util.filename(node)

    s = node.xpath('./src:name/text()',
        namespaces=util.srcml_ns())

    if (len(s) <= 0):
        s = node.xpath('./src:name/src:name/text()',
        namespaces=util.srcml_ns())

    info += ": " + s[0]
    print(info)
