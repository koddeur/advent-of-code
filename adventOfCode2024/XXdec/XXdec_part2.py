#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def xxx_yyy_part2(file):
    """
    xxx yyy part two

    Args : 
    file -- the input file

    Return : 
    count -- the result
    """
    count=0

    f = open(file, "r")
    line=f.readline()
    while (line != ''):
        line=f.readline()

    return count

def main():
    print('# Day XX - part 2')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(xxx_yyy_part2(arg1)))

if __name__=="__main__":
    main()