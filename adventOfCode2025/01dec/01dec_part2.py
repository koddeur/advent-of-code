#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def secret_entrance_part2(file):
    """
    Secret entrance part two

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0
    position=50

    f = open(file, "r")
    line=f.readline()
    while (line != ''):
        
        if (line[-1] == '\n') :
            line=line[:-1]
        
        rotation=line[0]
        increment=int(line[1:])
        
        if (rotation == "R"):
            i=0
            while(i < increment):
                i+=1
                
                if(position+1 == 100):
                    count+=1
                    
                if((position + 1) == 100):
                    position = 0
                else :
                    position += 1
            
        else :
            i=0
            while(i < increment):
                i+=1
                
                if(position-1 == 0):
                    count+=1
                    
                if((position - 1) == -1):
                    position = 99
                else :
                    position = position - 1

        line = f.readline()
    return count

# TESTS LILAS
dialPosition=50
zeroCount=0

def test(file):
    global zeroCount

    f = open(file, "r")
    line=f.readline()
    
    while (line != ''):
        
        if (line[-1] == '\n') :
            line=line[:-1]
        rotation=line[0]
        increment=int(line[1:])
        
        if (rotation == "R"):
            rotRight(increment)
        else :
            rotLeft(increment)
        print("DIAL POSITION : " + str(dialPosition))
            
        line = f.readline()
    return zeroCount
            

def rotLeft(leftTurns):
    global dialPosition
    global zeroCount
    
    dialPosition = dialPosition - leftTurns
    while (dialPosition < 0):
        if (dialPosition==-100):
            print('hellloooooo -100')
        dialPosition += 100
        zeroCount+=1
        print("L - je suis de passage sur 0 --> " + str(dialPosition))

        
    
    if (dialPosition == 0):
        zeroCount+=1
        print("R - je m'arrete sur 0 --> " + str(dialPosition))
        
    
def rotRight(rightTurns):
    global dialPosition
    global zeroCount
    dialPosition = dialPosition + rightTurns
    while (dialPosition > 100):
        dialPosition -= 100
        zeroCount+=1
        print("R - je suis de passage sur 0 --> " + str(dialPosition))
    
    if (dialPosition == 100):
        dialPosition = 0
    
    if (dialPosition == 0):
        zeroCount+=1
        print("R - je m'arrete sur 0 --> " + str(dialPosition))
    

def main():
    print('# Day 01 - part 2')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(test(arg1)))

if __name__=="__main__":
    main()