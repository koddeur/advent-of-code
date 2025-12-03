#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def sonar_sweep_part1(file):
    """
    Sonar sweep part one

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0
    last_measurement=0

    f = open(file, "r")
    line=f.readline().replace("\n","")
    line=f.readline().replace("\n","")
    while (line != ''):
        new_measurement=int(line)
        
        if(new_measurement > last_measurement):
            count+=1 
        last_measurement=new_measurement
            
        line = f.readline().replace("\n","")
    return count

def main():
    print('# Day 01 - part 1')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(sonar_sweep_part1(arg1)))

if __name__=="__main__":
    main()