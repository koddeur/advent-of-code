#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def is_a_report_safe(report):
    """
    Determine if a report is safe or not

    Args : 
    report -- list of levels

    Return : 
    boolean -- True if the report is safe, False otherwise
    """
    decreasing=False
    increasing=False
    first_level=int(report[0])
    second_level=int(report[1])

    if first_level > second_level : 
        decreasing=True
    elif first_level < second_level: 
        increasing=True

    if(decreasing or increasing):
        i=0
        error=False
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
        if (decreasing or increasing):
            return True
        else : 
            return False


def red_nosed_reports_part2(file):
    """
    Red-Nosed Reports part two

    Args : 
    file -- the input file

    Return : 
    count -- number of reports safe
    """
    count=0

    f = open(file, "r")
    line=f.readline()
    while (line != ''):
        if line[-1] == "\n" : 
            report = line[:-1].split(" ")
        else: 
            report = line.split(" ")
        
        if is_a_report_safe(report) :
            count+=1
        else :
            i=0
            for level in report:
                newreport=report[:i]+report[i+1:]
                if is_a_report_safe(newreport):
                    count+=1
                    break
                i+=1
        
        line=f.readline()

    return count

def main():
    print('# Day 02 - part 2')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(red_nosed_reports_part2(arg1)))

if __name__=="__main__":
    main()