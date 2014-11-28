# Input: Source code in XML
# Output: Classes with more than n fields

import util
from lxml import etree

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
            print(etree.tostring(child))

    print(num)
