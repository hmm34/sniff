# Input: Source code in XML
# Output: Classes with more than n fields

import util
from lxml import etree

tree = util.inputtree()

#<decl_stmt><decl><type><name>
#/DocText/WithQuads/Page/Word[text()='July' and Quad/P1/@X > 90]
#[text()[normalize-space(.)='July']
query = "//*[src:decl_stmt/src:decl/src:type/src:name"
query += "/text()[normalize-space(.)='class']]"

r = tree.xpath(query,
    namespaces={'src': 'http://www.sdml.info/srcML/src',
                'cpp': 'http://www.sdml.info/srcML/cpp'})

num = 0
for node in r:
    s = node.xpath('.//*[not(.//src:argument)]/src:expr[not(.//src:argument_list)]',
        namespaces={'src': 'http://www.sdml.info/srcML/src',
                    'cpp': 'http://www.sdml.info/srcML/cpp'})
    for child in s:
        num += 1
        print(etree.tostring(child))

print(len(r))
print(num)
