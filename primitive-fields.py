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
query = "//*[src:decl_stmt/src:decl/src:type/src:name"
query += "/text()[normalize-space(.)='class']]"
r = tree.xpath(query,
    namespaces={'src': 'http://www.sdml.info/srcML/src',
                'cpp': 'http://www.sdml.info/srcML/cpp'})

for node in r:
    num = 0

    # only use fields
    primitives = ""
    s = node.xpath('.//src:expr[not(.//src:argument_list)]',
        namespaces={'src': 'http://www.sdml.info/srcML/src',
                    'cpp': 'http://www.sdml.info/srcML/cpp'})

    primitives = ""
    for child in s:
        p = child.getparent()
        if util.get_bare_tag(p) != 'argument':
        	primitives += etree.tostring(child, method="text")
        	#parts = ([child.text] +
            #list(chain(*([c.text, etree.tostring(c), c.tail] for c in child.getchildren()))) + [node.tail])

		    # filter removes possible Nones in texts and tails
		    #parts = ''.join(filter(None, parts))
		    #print(parts.tostring())
        	num += 1

    # exceeds threshold
    if num > n:
        info = node.get('filename')

        query = ".//src:decl_stmt/src:decl[src:type/src:name"
        query += "/text()[normalize-space(.)='class']]/src:name/text()"
        u = tree.xpath(query,
            namespaces={'src': 'http://www.sdml.info/srcML/src',
                        'cpp': 'http://www.sdml.info/srcML/cpp'})

        info += ": " + (u[1]) + '\n' + primitives
        print(info)
