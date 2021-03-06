# Input: Source code in XML
# Output: Class names with primitive fields > n

import argparse
import util
from lxml import etree

parser = util.parser("threshold primitive field count for classes")
n = parser.parse_args().n

tree = util.inputtree()

# get classes
r = tree.xpath("//src:class",
    namespaces=util.srcml_ns())

for node in r:
    num = 0

    # only count primitive fields
    core_query = ".//src:decl_stmt[src:decl/src:type/src:name/text()='"
    types = util.primitives()

    query = ""
    for i in range(0, len(types)):
        query += core_query + types[i] + "']"
        if i != len(types) - 1:
            query += " | "

    s = node.xpath(query,
        namespaces=util.srcml_ns())

    num = len(s)

    # exceeds threshold
    if num > n:
        file_name = util.filename(node)

        class_name = node.xpath('./src:name/text()',
            namespaces=util.srcml_ns())
        info = file_name + ": " + class_name[0]
        print(info)
