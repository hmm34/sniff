# Input: Source code in XML
# Output: Number of line and block comments

import util

tree = util.inputtree()

r = tree.xpath('//src:comment',
    namespaces={'src': 'http://www.sdml.info/srcML/src',
                'cpp': 'http://www.sdml.info/srcML/cpp'})

print(len(r))
