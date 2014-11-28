# Input: Source code in XML
# Output: Function names whose contents exceed n lines

import argparse
import util
from lxml import etree

parser = argparse.ArgumentParser(description = 'Sniff out code smells')
parser.add_argument('n',
                    help = "threshold line count for long methods",
                    type = int)
n = parser.parse_args().n

tree = util.inputtree()

r = tree.xpath('//src:function | //src:constructor',
    namespaces={'src': 'http://www.sdml.info/srcML/src',
                'cpp': 'http://www.sdml.info/srcML/cpp'})

for node in r:
    string = etree.tostring(node)
    if string.count('\n') > n:
        s = node.xpath('(./src:name/src:name/text())[last()]',
            namespaces={'src': 'http://www.sdml.info/srcML/src',
                        'cpp': 'http://www.sdml.info/srcML/cpp'})
        print(s[0])
