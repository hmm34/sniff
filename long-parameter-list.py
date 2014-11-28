# Input: Source code in XML
# Output: Function names matching a parameter list > n

import argparse
import util

parser = argparse.ArgumentParser(description = 'Sniff out code smells')
parser.add_argument('n',
                    help = "threshold parameter count for methods",
                    type = int)
n = parser.parse_args().n

tree = util.inputtree()

predicate = '[count(src:parameter_list/src:param) > ' + `n` + ' ]'
query = '//src:function' + predicate + ' | //src:constructor' + predicate

r = tree.xpath(query,
    namespaces={'src': 'http://www.sdml.info/srcML/src',
                'cpp': 'http://www.sdml.info/srcML/cpp'})

for node in r:
    s = node.xpath('(./src:name/src:name/text())[last()]',
        namespaces={'src': 'http://www.sdml.info/srcML/src',
                    'cpp': 'http://www.sdml.info/srcML/cpp'})
    print(s[0])
