#!/usr/bin/env python3 
# author : Mael Avennec

import sys

board={}
lengthUniverse=0
heightUniverse=0
countNoGalaxyRows=0
countNoGalaxyColumns=0

def cosmicExpansion_partOne(file):
    """
    Cosmic Expansion enigma part one

    Args :
    file (str) -- the input file path
    
    Return :
    count (int) -- the result of the sum of the shortest path between all pairs of galaxies
    """
    global board
    global lengthUniverse
    global heightUniverse
    global countNoGalaxyRows
    global countNoGalaxyColumns

    parse_input(file)
    printBoard()
    
    # Add empty column
    for x in range(lengthUniverse+countNoGalaxyColumns):
        isEmptyColumn=True
        y=0
        while y<heightUniverse and isEmptyColumn!=False:
            if (board[(x,y)]=='#'):
                isEmptyColumn=False
            y+=1
        if(isEmptyColumn==True):
            for xNew in range(x+1,lengthUniverse+countNoGalaxyColumns):
                print(xNew)
                for yNew in range(heightUniverse):
                    if((xNew+1,yNew) not in board.keys()):
                        board[(xNew+1,yNew)]='.'
                    board[(xNew,yNew)]=board[(xNew+1,yNew)]

    print(board)
    print(lengthUniverse)
    print(heightUniverse)
    print(countNoGalaxyRows)
    print(countNoGalaxyColumns)
    printBoard()
    return 0

def printBoard():
    """
    """
    global board

    output=""
    for y in range(heightUniverse) : 
        for x in range(lengthUniverse) :
            output+=board[(x,y)]
        output+="\n"
    print(output)


def parse_input(file_path):
    """
    """
    global board
    global lengthUniverse
    global heightUniverse
    global countNoGalaxyRows
    global countNoGalaxyColumns

    f = open(file_path, "r")
    line=f.readline()
    line=line.replace('\n','')

    lengthUniverse=len(line)

    y=0
    while (line != '') : 
        line=line.replace('\n','')
  
        isEmptyRow=True
        x=0
        while x<len(line):
            if(line[x]=='#'):
                isEmptyRow=False
            board[(x,y)]=line[x]
            x+=1
        if(isEmptyRow):
            countNoGalaxyRows+=1
        y+=1
        line = f.readline()
    heightUniverse=y
    
    # Count empty columns
    for x in range(lengthUniverse) :
        isGalaxyFound=False
        y=0
        while (y<heightUniverse and isGalaxyFound!=True) :
            if board[(x,y)]=='#' :
                isGalaxyFound=True
            y+=1

        if not(isGalaxyFound):
            countNoGalaxyColumns+=1

    f.close()

def main():
    arg1 = sys.argv[1]
    print('# Day 11 - part 1')
    print('-----------------')
    print('Result => {}'.format(cosmicExpansion_partOne(arg1)))

if __name__=="__main__":
    main()

