#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def print_queue_part2(file):
    """
    Print Queue part two

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0

    f = open(file, "r")
    line=f.readline()
    while (line != ''):
        line=f.readline()

    return count

def main():
    print('# Day 05 - part 2')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(print_queue_part2(arg1)))

if __name__=="__main__":
    main()