# Input: Source code in XML
# Output: Function names whose contents exceed n lines. Content includes
#   the line on which the function is defined, and lines with brackets.

import argparse
import util
from lxml import etree

parser = util.parser("threshold line count for long methods")
n = parser.parse_args().n

tree = util.inputtree()

r = tree.xpath('//src:function | //src:constructor',
    namespaces={'src': 'http://www.sdml.info/srcML/src',
                'cpp': 'http://www.sdml.info/srcML/cpp'})

for node in r:
    string = etree.tostring(node)
    if string.count('\n') > n:
        info = filename(node)

        s = node.xpath('(./src:name/src:name/text())[last()]',
            namespaces={'src': 'http://www.sdml.info/srcML/src',
                        'cpp': 'http://www.sdml.info/srcML/cpp'})

        # In case a static function was encountered
        if (len(s) <= 0):
            s = node.xpath('(./src:name/text())[last()]',
            namespaces={'src': 'http://www.sdml.info/srcML/src',
                        'cpp': 'http://www.sdml.info/srcML/cpp'})

        info += ": " + s[0]
        print(info)
