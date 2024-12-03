#!/usr/bin/env python3 
# author : Mael Avennec

import sys,re

def mull_it_over_part2(file):
    """
    Mull It Over part two

    Args : 
    file -- the input file

    Return : 
    count -- the operationult
    """
    count=0

    f = open(file, "r")
    line=f.readline()
    instruction=True
    
    while (line != ''):
        pattern = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"
        operations = re.findall(pattern, line)
        
        for operation in operations :
            if operation == "do()" :
                instruction = True
            elif operation == "don't()" : 
                instruction = False
            else :
                if instruction :
                    numbers=operation.replace('mul(','').replace(')','').split(',')
                    count += int(numbers[0]) * int(numbers[1])
        
        line=f.readline()

    return count

def main():
    print('# Day 03 - part 2')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(mull_it_over_part2(arg1)))

if __name__=="__main__":
    main()