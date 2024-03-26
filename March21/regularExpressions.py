# need to import re in your program before using
# re.search() to see if a string matches the regEX, like find() for strings
# re.finall() to extract portions of a string that match your regEX, similar to find() and slicing var[5:10]

import re

hand = open('test.txt')
    for line in hand:
        line = line.rstrip()
        if re.search('a', line):
            print(line)

            
hand = open('test.txt')
    for line in hand:
        line = line.rstrip()
        if re.search('^a', line):
            print(line)
