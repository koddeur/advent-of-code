#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def isCoordinateInThePuzzle(coordinate, max_length, max_height):
    """
    Check if the coordinate is inside the limit

    Args:
        coordinate (tuple): the coordinate of the letter
        max_length (int): the length limit
        max_height (int): the height limit

    Returns:
        boolean: True if the coordinate is inside the puzzle, False otherwise
    """
    if (coordinate[0] >=0 and coordinate[0] <= max_length) and (coordinate[1] >=0 and coordinate[1] <= max_height) :
        return True
    return False

def remove_line_break(line):
    """
    Remove line break of line

    Args:
        line (String): line of file
    """
    if (line != '' and line[-1] == "\n"): 
            line = line[:-1]
    return line

def fill_puzzle(file):
    """
    Fill the puzzle in a dict

    Args:
        file (String): file name

    Returns:
        dict: the puzzle
    """
    puzzle=dict()
    f = open(file, "r")
    line=remove_line_break(f.readline())
    y=0
    while (line != ''):
        x=0
        while x < len(line) : 
            puzzle[(x,y)]=line[x]
            x+=1
        y+=1
        line=remove_line_break(f.readline())   
    f.close()
    
    return puzzle

def ceres_search_part2(file):
    """
    Ceres Search part two

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0
    puzzle=fill_puzzle(file)
    
    count_lines = sum(1 for _ in open(file))-1
    count_letters = len(remove_line_break(open(file, "r").readline()))-1
    
    for letter in puzzle : 
        if puzzle[letter] == 'A' :
            isXmas=True
            test_coordinate=(letter[0]-1,letter[1]-1)
            if isCoordinateInThePuzzle(test_coordinate,count_letters,count_lines) and (puzzle[test_coordinate]=='M' or puzzle[test_coordinate]=='S'):
                opposite_coordinate=(letter[0]+1,letter[1]+1)
                if isCoordinateInThePuzzle(opposite_coordinate,count_letters,count_lines):
                    if(puzzle[test_coordinate]=='M'):
                        if(puzzle[opposite_coordinate]!='S'):
                            isXmas=False
                    if(puzzle[test_coordinate]=='S'):
                        if(puzzle[opposite_coordinate]!='M'):
                            isXmas=False
                else:
                    isXmas=False
            else:
                isXmas=False
            
            test_coordinate=(letter[0]+1,letter[1]-1)
            if isCoordinateInThePuzzle(test_coordinate,count_letters,count_lines) and (puzzle[test_coordinate]=='M' or puzzle[test_coordinate]=='S'):
                opposite_coordinate=(letter[0]-1,letter[1]+1)
                if isCoordinateInThePuzzle(opposite_coordinate,count_letters,count_lines):
                    if(puzzle[test_coordinate]=='M'):
                        if(puzzle[opposite_coordinate]!='S'):
                            isXmas=False
                    if(puzzle[test_coordinate]=='S'):
                        if(puzzle[opposite_coordinate]!='M'):
                            isXmas=False
                else : 
                    isXmas=False
            else:
                isXmas=False
        
            if isXmas==True :
                count+=1    
    return count

def main():
    print('# Day 04 - part 2')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(ceres_search_part2(arg1)))

if __name__=="__main__":
    main()