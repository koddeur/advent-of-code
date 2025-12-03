#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def gift_shop_part1(file):
    """
    Gift shop part one

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0

    f = open(file, "r")
    line=f.readline()[:-1]
    ranges = line.split(',')
    for range in ranges :
        id_first = int(range.split('-')[0])
        id_second = int(range.split('-')[1])
        i=id_first
        while i <= id_second :
            l = len(str(i))
            mid = int(l/2)
            if (l % 2) == 0 : 
                f = str(i)[:mid]
                s = str(i)[mid:]
                if (int(f) - int(s) == 0):
                    count+=i
            i+=1        
    return count

def main():
    print('# Day 02 - part 1')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(gift_shop_part1(arg1)))

if __name__=="__main__":
    main()