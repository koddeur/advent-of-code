#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def xxxYYY_partOne(file):
    """
    xxx YYY part one

    Args : 
    file -- the input file

    Return : 
    count -- 
    """
    f = open(file, "r")
    line=f.readline()
    count=0
    while (line != ''):

        line=f.readline()

    return count

def main():
    print('# Day XX - part 1')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(xxxYYY_partOne(arg1)))

if __name__=="__main__":
    main()