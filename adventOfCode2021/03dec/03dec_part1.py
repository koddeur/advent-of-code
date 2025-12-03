#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def binary_diagnostic_part1(file):
    """
    Binary diagnostic part one

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0
    gamma_rate=""
    epsilon_rate=""
    tableaux=[]

    f = open(file, "r")
    line=f.readline().replace("\n","")
    n=len(line)
    
    # Create n dict 
    for i in range(n):
        tableaux.append({"0":0,"1":0})
    
    while (line != ''):
        for j in range(n):
            tableaux[j][line[j]]+=1        
        line=f.readline().replace("\n","")
        
    for gamma in tableaux:
        gamma_rate += max(gamma, key=gamma.get)
        epsilon_rate += min(gamma, key=gamma.get)
    
    count = int(gamma_rate, 2) * int(epsilon_rate, 2)

    return count

def main():
    print('# Day 03 - part 1')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(binary_diagnostic_part1(arg1)))

if __name__=="__main__":
    main()