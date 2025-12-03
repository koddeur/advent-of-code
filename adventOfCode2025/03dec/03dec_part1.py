#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def lobby_part1(file):
    """
    Lobby part one

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0

    f = open(file, "r")
    line=f.readline().replace("\n","")
    while (line != ''):
        bank = [int(i) for i in line]   
        
        first_max_digit=max(bank[:-1]) 
        index_max = bank.index(first_max_digit)+1
        second_max_digit=max(bank[index_max:])
        
        jolts = int(str(first_max_digit)+str(second_max_digit))
        
        count+=jolts
        
        line=f.readline().replace("\n","")

    return count

def main():
    print('# Day 03 - part 1')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(lobby_part1(arg1)))

if __name__=="__main__":
    main()