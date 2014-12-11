# Input: Source code in XML
# Output: Class names with primitive fields > n

import argparse
import util
from lxml import etree

parser = util.parser()
parser.add_argument('n',
                    help = "threshold primitive field count for classes",
                    type = int)
n = parser.parse_args().n

tree = util.inputtree()

# get classes
r = tree.xpath("//src:class",
    namespaces={'src': 'http://www.sdml.info/srcML/src',
                'cpp': 'http://www.sdml.info/srcML/cpp'})

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
        namespaces={'src': 'http://www.sdml.info/srcML/src',
                    'cpp': 'http://www.sdml.info/srcML/cpp'})

    num = len(s)

    # exceeds threshold
    if num > n:
        p = node.getparent()
        while p.getparent().getparent() is not None:
            p = p.getparent()
        file_name = p.get('filename')

        class_name = node.xpath('./src:name/text()',
            namespaces={'src': 'http://www.sdml.info/srcML/src',
                        'cpp': 'http://www.sdml.info/srcML/cpp'})
        info = file_name + ": " + class_name[0]
        print(info)
