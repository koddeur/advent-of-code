#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def redNosedReports_partOne(file):
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
        levels = line.split(" ")
        decreasing=False
        increasing=False
        if int(levels[0]) > int(levels[1]) : 
            decreasing=True
        elif int(levels[0]) < int(levels[1]): 
            increasing=True

        if(decreasing or increasing):
            i=0
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
            if (decreasing or increasing) :
                count+=1

        line=f.readline()

    return count

def main():
    print('# Day 02 - part 1')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(redNosedReports_partOne(arg1)))

if __name__=="__main__":
    main()