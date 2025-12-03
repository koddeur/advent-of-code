#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def secret_entrance_part1(file):
    """
    Secret entrance part one

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0
    position=50

    f = open(file, "r")
    line=f.readline().replace("\n","")
    while (line != ''):   
         
        rotation=line[0]
        increment=int(line[1:])
        
        if (rotation == "R"):
            i=0
            while(i < increment):
                i+=1
                if((position + 1) == 100):
                    position = 0
                else :
                    position += 1
        else :
            i=0
            while(i < increment):
                i+=1
                if((position - 1) == -1):
                    position = 99
                else :
                    position = position - 1

        if(position == 0):
            count+=1
            
        line = f.readline().replace("\n","")
    return count

def main():
    print('# Day 01 - part 1')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(secret_entrance_part1(arg1)))

if __name__=="__main__":
    main()