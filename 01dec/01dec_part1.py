#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def historianHysteria_partOne(file):
    """
    Historian hysterian part one

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

    first_list.sort()
    second_list.sort()

    i=0
    while i<len(first_list):
        diff=max(first_list[i],second_list[i])-min(first_list[i],second_list[i])
        count+=diff
        i+=1

    return count

def main():
    print('# Day 01 - part 1')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(historianHysteria_partOne(arg1)))

if __name__=="__main__":
    main()