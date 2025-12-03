#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def dive_part1(file):
    """
    Dive part one

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0
    horizontal=0
    depth=0

    f = open(file, "r")
    line=f.readline().replace("\n","")
    while (line != ''):
        
        direction=line.split(" ")[0]
        distance=int(line.split(" ")[1])
        
        match direction:
            case "forward" :
                horizontal+=distance
            case "down" :
                depth += distance
            case "up" : 
                depth -= distance
            
        line=f.readline().replace("\n","")
        
    count=horizontal*depth

    return count

def main():
    print('# Day 02 - part 1')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(dive_part1(arg1)))

if __name__=="__main__":
    main()