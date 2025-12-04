#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def printing_department_part1(file):
    """
    Printing Department part one

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0
    coordinates={}

    f = open(file, "r")
    line=f.readline().replace("\n","")
    x_max=len(line)-1
    y_max=0
    
    i=0
    while (line != ''):
        for j in range(len(line)):
            coordinates[(int(j),i)]=line[j]
        line=f.readline().replace("\n","")
        i+=1
        
    y_max = i-1        
    for coordinate in coordinates.keys() : 
        rolls_of_paper=0
        
        y=-1
        while y<=1:
            x=-1
            while x<=1:
                if not(y==0 and x==0):
                    if ((coordinate[0] + x)>=0) and ((coordinate[0] + x)<= x_max) and ((coordinate[1] + y)>=0) and ((coordinate[1] + y)<= y_max) :
                        if(coordinates[coordinate[0]+x, coordinate[1]+y] == "@"):
                            rolls_of_paper+=1
                x+=1
            y+=1
        
        if(coordinates[coordinate] == '@' and rolls_of_paper<4):
            count+=1

    return count

def main():
    print('# Day 04 - part 1')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(printing_department_part1(arg1)))

if __name__=="__main__":
    main()