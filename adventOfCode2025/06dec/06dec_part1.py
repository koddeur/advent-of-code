#!/usr/bin/env python3 
# author : Mael Avennec

import sys
import math

def trash_compactor_part1(file):
    """
    Trash Compactor part one

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0
    problems=[]
    problem_results=[]

    f = open(file, "r")
    line=f.readline().replace("\n","")
    line_items=[item for item in line.split(" ") if item != '']
    nb_of_problems=len(line_items)
    
    for i in range(nb_of_problems):
        problems.append(list())

    # For each line, add the digit to the right problem
    while (line != ''):
        for i in range(nb_of_problems) : 
            match line_items[i]:
                case "*" :
                    problems[i].append(line_items[i])
                case "+" : 
                    problems[i].append(line_items[i])
                case _:
                    problems[i].append(int(line_items[i]))
        
        # Read next line
        line=f.readline().replace("\n","")
        line_items=[item for item in line.split(" ") if item != '']
        
    # Calculate each problem
    for i in range(nb_of_problems):
        match problems[i][-1]:
                case "*" :
                    problem_results.append(math.prod(problems[i][:-1]))
                case "+" : 
                    problem_results.append(sum(problems[i][:-1]))
                    
    count = sum(problem_results)

    return count

def main():
    print('# Day 06 - part 1')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(trash_compactor_part1(arg1)))

if __name__=="__main__":
    main()