#!/usr/bin/env python3 
# author : Mael Avennec

import sys
import re

def mull_it_over_part1(file):
    """
    Mull It Over part one

    Args : 
    file -- the input file

    Return : 
    count -- the operationult
    """
    count=0

    f = open(file, "r")
    line=f.readline()
    while (line != ''):
        pattern= r"mul\(\d+,\d+\)"
        operations = re.findall(pattern, line)
        
        for operation in operations :
            numbers=operation.replace('mul(','').replace(')','').split(',')
            count+=int(numbers[0])*int(numbers[1])
        
        line=f.readline()
    return count

def main():
    print('# Day 03 - part 1')
    print('-----------------')
    arg1 = sys.argv[1]
    print('operationult => {}'.format(mull_it_over_part1(arg1)))

if __name__=="__main__":
    main()