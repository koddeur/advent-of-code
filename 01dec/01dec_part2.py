#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def historianHysteria_partTwo(file):
    """
    Historian hysterian part two

    Args : 
    file -- the input file

    Return : 
    count -- the total distance
    """
    f = open(file, "r")
    line=f.readline()
    count=0
    first_list=[]
    second_list=[]
    while (line != ''):
        first_number=line.split("   ")[0]
        first_list.append(int(first_number))
        second_number=line.split("   ")[1]
        second_list.append(int(second_number))

        line=f.readline()

    i=0
    while i<len(first_list):
        similarity=second_list.count(first_list[i])
        count+=first_list[i]*similarity
        i+=1

    return count

def main():
    print('# Day 01 - part 2')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(historianHysteria_partTwo(arg1)))

if __name__=="__main__":
    main()