#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def red_nosed_reports_part1(file):
    """
    Red-Nosed Reports part one

    Args : 
    file -- the input file

    Return : 
    count -- number of reports safe
    """
    count=0
    f = open(file, "r")
    line=f.readline()
    
    while (line != ''):
        report = line.split(" ")
        decreasing=False
        increasing=False
        if int(report[0]) > int(report[1]) : 
            decreasing=True
        elif int(report[0]) < int(report[1]): 
            increasing=True

        if(decreasing or increasing):
            i=0
            while i < len(report)-1:
                level_a = int(report[i])
                level_b = int(report[i+1])

                if decreasing :
                    if (level_a <= level_b) or abs(level_a-level_b)>3:
                        decreasing=False
                        break
                elif increasing :
                    if (level_a >= level_b) or abs(level_a-level_b)>3:
                        increasing=False
                        break
                i+=1
            if (decreasing or increasing) :
                count+=1

        line=f.readline()

    return count

def main():
    print('# Day 02 - part 1')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(red_nosed_reports_part1(arg1)))

if __name__=="__main__":
    main()