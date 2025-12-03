#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def dive_part2(file):
    """
    Dive part two

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0
    horizontal=0
    depth=0
    aim=0

    f = open(file, "r")
    line=f.readline().replace("\n","")
    while (line != ''):
        
        direction=line.split(" ")[0]
        distance=int(line.split(" ")[1])
        
        match direction:
            case "forward" :
                horizontal+=distance
                depth += aim*distance
            case "down" :
                aim += distance
            case "up" : 
                aim -= distance
            
        line=f.readline().replace("\n","")
        
    count=horizontal*depth

    return count

def main():
    print('# Day 02 - part 2')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(dive_part2(arg1)))

if __name__=="__main__":
    main()