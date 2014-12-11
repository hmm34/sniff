# Input: Source code in XML
# Output: Classes with more than n fields

import argparse
import util
from lxml import etree

parser = util.parser("threshold field count for a class")
n = parser.parse_args().n

tree = util.inputtree()

r = tree.xpath("//src:class",
    namespaces={'src': 'http://www.sdml.info/srcML/src',
                'cpp': 'http://www.sdml.info/srcML/cpp'})

for node in r:
    s = node.xpath('.//src:decl_stmt',
        namespaces={'src': 'http://www.sdml.info/srcML/src',
                    'cpp': 'http://www.sdml.info/srcML/cpp'})
    num = len(s) 

    if num > n:
        file_name = util.filename(node)

        class_name = node.xpath('./src:name/text()',
             namespaces={'src': 'http://www.sdml.info/srcML/src',
                         'cpp': 'http://www.sdml.info/srcML/cpp'})[0]

        print(file_name + ": " + class_name)
