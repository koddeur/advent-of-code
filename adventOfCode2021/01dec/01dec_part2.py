#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def sonar_sweep_part2(file):
    """
    Sonar sweep part two

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0

    f = open(file, "r")
    measurements = [ligne.replace("\n","") for ligne in f.readlines()] # Read all values
    
    f.seek(0) # Back to the beginning of the file
    
    i=1
    last_three_measurement=0
    while i < len(measurements)-2:
        three_measurement=int(measurements[i])+int(measurements[i+1])+int(measurements[i+2])
        if three_measurement > last_three_measurement :
            count+=1
        last_three_measurement = three_measurement
        
        i+=1 
    return count

def main():
    print('# Day 01 - part 2')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(sonar_sweep_part2(arg1)))

if __name__=="__main__":
    main()