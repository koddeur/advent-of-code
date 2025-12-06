#!/usr/bin/env python3 
# author : Mael Avennec

import sys
import math

def trash_compactor_part2(file):
    """
    Trash Compactor part two

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0
    problems=[]
    problem_results=[]

    f = open(file, "r")
    last_line = f.readlines()[-1]
    f.seek(0)
    line=f.readline().replace("\n","")
    
    # Retrieve the number of problems by sign
    i=0
    maliste=[]
    while i<len(last_line):
        
        if(last_line[i] != ' '):
            if(i!=0):
                maliste.append(j)
            j=0
        else :
            j+=1
        i+=1
        
        if(i == len(last_line)):
            maliste.append(j+1)

    # Create the problems with the right number of problem
    for m in range(len(maliste)):
        numbers = []
        for l in range(maliste[m]):
            numbers.append("")
        problems.append(numbers)
      
    # For each line, add the digit to the right problem
    while (line != ''):
        i=0
        j=0
        k=0
        while i<len(line):
            if line[i] != " ":
                problems[k][j]+=line[i]
            
            if(j==maliste[k]-1):
                j=0
                i+=1
                k+=1
            else : 
                j+=1
            i+=1    
        line=f.readline().replace("\n","")
      
    # Calculate the result of the problems
    for problem in problems:
        match problem[0][-1]:
            case "*" :
                problem = [int(item.replace("*","")) for item in problem]
                problem_results.append(math.prod(problem))
            case "+" :
                problem = [int(item.replace("+","")) for item in problem]
                problem_results.append(sum(problem))
                    
    count = sum(problem_results)

    return count

def main():
    print('# Day 06 - part 2')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(trash_compactor_part2(arg1)))

if __name__=="__main__":
    main()