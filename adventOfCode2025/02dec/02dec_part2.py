#!/usr/bin/env python3 
# author : Mael Avennec

import sys
from sympy import divisors
import textwrap

def gift_shop_part2(file):
    """
    Gift shop part two

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0

    f = open(file, "r")
    line=f.readline()
    ranges = line.split(',')
    for range in ranges :
        id_first = int(range.split('-')[0])
        id_second = int(range.split('-')[1])
        i=id_first
        while i <= id_second :
            l = len(str(i))
            divs = divisors(l)[:-1]
            for div in divs : 
                parts = textwrap.wrap(str(i), div)
                if (len(set(parts)) == 1): 
                    count+=i
                    divs.clear()
            i+=1        
    return count

def main():
    print('# Day 02 - part 2')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(gift_shop_part2(arg1)))

if __name__=="__main__":
    main()