#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def lobby_part2(file):
    """
    Lobby part two

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0

    f = open(file, "r")
    line=f.readline().replace("\n","")
    while (line != ''): 
        jolts = ""
        bank = [int(i) for i in line]  
        
        i=0
        j=11
        first_index=0
        while i < 12 : 
            last_index = len(bank) - j
            max_digit = max(bank[first_index:last_index])
            index_max = first_index + bank[first_index:last_index].index(max_digit)+1
            first_index = index_max
            jolt_digit = max_digit
            
            jolts += str(jolt_digit)
            
            i+=1
            j-=1        
            
        count+=int(jolts)
        
        line=f.readline().replace("\n","")

    return count

def main():
    print('# Day 03 - part 2')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(lobby_part2(arg1)))

if __name__=="__main__":
    main()