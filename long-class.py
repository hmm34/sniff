# Input: Source code in XML
# Output: Classes with more than n fields

import argparse
import util
from lxml import etree

parser = argparse.ArgumentParser(description = 'Sniff out code smells')
parser.add_argument('n',
                    help = "threshold field count for a class",
                    type = int)
n = parser.parse_args().n

tree = util.inputtree()

query = "//*[src:decl_stmt/src:decl/src:type/src:name"
query += "/text()[normalize-space(.)='class']]"

r = tree.xpath(query,
    namespaces={'src': 'http://www.sdml.info/srcML/src',
                'cpp': 'http://www.sdml.info/srcML/cpp'})

for node in r:
    num = 0
    s = node.xpath('.//src:expr[not(.//src:argument_list)]',
        namespaces={'src': 'http://www.sdml.info/srcML/src',
                    'cpp': 'http://www.sdml.info/srcML/cpp'})
    for child in s:
        p = child.getparent()

        if util.get_bare_tag(p) != 'argument':
            num += 1

    if num > n:
        info = node.get('filename')

        query = ".//src:decl_stmt/src:decl[src:type/src:name"
        query += "/text()[normalize-space(.)='class']]/src:name/text()"
        u = tree.xpath(query,
            namespaces={'src': 'http://www.sdml.info/srcML/src',
                        'cpp': 'http://www.sdml.info/srcML/cpp'})

        info += ": " + (u[0])
        print(info)
