#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def is_coordinate_in_the_puzzle(coordinate, max_length, max_height):
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

def ceres_search_part1(file):
    """
    Ceres Search part one

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
        if puzzle[letter] == 'X' :
            x=-1
            while x <= 1:
                y=-1
                while y <= 1:
                    next_coordinate=(letter[0]+x,letter[1]+y)
                    if is_coordinate_in_the_puzzle(next_coordinate,count_letters,count_lines) :
                        
                        if puzzle[(next_coordinate[0],next_coordinate[1])]=='M':
                            dir=(x,y)
                            next_coordinate=(next_coordinate[0]+dir[0], next_coordinate[1]+dir[1])
                            
                            if is_coordinate_in_the_puzzle((next_coordinate[0],next_coordinate[1]),count_letters,count_lines):
                                if puzzle[(next_coordinate[0],next_coordinate[1])]=='A':
                                    next_coordinate=(next_coordinate[0]+dir[0], next_coordinate[1]+dir[1])
                                    
                                    if is_coordinate_in_the_puzzle((next_coordinate[0],next_coordinate[1]),count_letters,count_lines):
                                        if puzzle[(next_coordinate[0],next_coordinate[1])]=='S':
                                            count+=1
                    y+=1
                x+=1
    return count

def main():
    print('# Day 04 - part 1')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(ceres_search_part1(arg1)))

if __name__=="__main__":
    main()