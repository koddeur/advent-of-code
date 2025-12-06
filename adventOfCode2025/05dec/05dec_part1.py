#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def cafeteria_part1(file):
    """
    Cafeteria part one

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0

    f = open(file, "r")
    lines = f.read().split("\n\n")
    ranges = lines[0].split("\n")
    ids = lines[1].split("\n")
    
    for id in ids:
        for id_range in ranges : 
            id_range_min=int(id_range.split("-")[0])
            id_range_max=int(id_range.split("-")[1])
            
            if (int(id) >= id_range_min and int(id) <= id_range_max) : 
                count+=1
                break

    return count

def main():
    print('# Day 05 - part 1')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(cafeteria_part1(arg1)))

if __name__=="__main__":
    main()