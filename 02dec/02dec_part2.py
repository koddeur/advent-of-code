#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def isOnlyDecreaseOrIncrease(levels):
    """
    """
    decreasing=False
    increasing=False
    if int(levels[0]) > int(levels[1]) : 
        decreasing=True
    elif int(levels[0]) < int(levels[1]): 
        increasing=True

    if(decreasing or increasing):
        i=0
        error=False
        while i < len(levels)-1:
            levelA = int(levels[i])
            levelB = int(levels[i+1])

            if decreasing :
                if (levelA <= levelB) or abs(levelA-levelB)>3:
                    decreasing=False
                    break
            elif increasing :
                if (levelA >= levelB) or abs(levelA-levelB)>3:
                    increasing=False
                    break
            i+=1
        if (decreasing or increasing):
            return True
        else : 
            return False


def redNosedReports_partTwo(file):
    """
    Red-Nosed Reports part two

    Args : 
    file -- the input file

    Return : 
    count -- 
    """
    count=0

    f = open(file, "r")
    line=f.readline()
    while (line != ''):
        if line[-1] == "\n" : 
            levels = line[:-1].split(" ")
        else: 
            levels = line.split(" ")
        
        if isOnlyDecreaseOrIncrease(levels) :
            count+=1
        else :
            i=0
            for level in levels:
                newLevels=levels[:i]+levels[i+1:]
                if isOnlyDecreaseOrIncrease(newLevels):
                    count+=1
                    break
                i+=1

        
        line=f.readline()

    return count

def main():
    print('# Day 02 - part 2')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(redNosedReports_partTwo(arg1)))

if __name__=="__main__":
    main()