# Input: Source code in XML
# Output: Class names with primitive fields > n

import argparse
import util
from lxml import etree

parser = argparse.ArgumentParser(description = 'Sniff out code smells')
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

    # only use fields
    s = node.xpath('.//src:decl_stmt',
        namespaces={'src': 'http://www.sdml.info/srcML/src',
                    'cpp': 'http://www.sdml.info/srcML/cpp'})

    num = len(s)
    primitives = ""
    for match in s:
        primitives += (etree.tostring(match, method="text").rstrip(' ').rstrip('\t'))

    # exceeds threshold
    if num > n:
        file_name = node.getparent().get('filename')
        class_name = node.xpath('./src:name/text()',
            namespaces={'src': 'http://www.sdml.info/srcML/src',
                        'cpp': 'http://www.sdml.info/srcML/cpp'})
        info = file_name + ": " + class_name[0]
        info += '\n' + primitives
        print(info)
