#!/usr/bin/env python3 
# author : Mael Avennec

import sys,math

def remove_line_break(line):
    """
    Remove line break of line

    Args:
        line (String): line of file
    """
    if (line != '' and line[-1] == "\n"): 
            line = line[:-1]
    return line

def fill_page_numbers(file):
    """_summary_

    Args:
        file (_type_): _description_

    Returns:
        _type_: _description_
    """
    page_numbers=dict()
    
    f = open(file, "r")
    line=remove_line_break(f.readline())
    
    while (line != ''):
        pages=line.split('|')
        
        if(pages[0] in page_numbers):
            page_numbers[pages[0]].append(pages[1])
        else : 
            page_numbers[pages[0]]=[pages[1]]
        
        line=remove_line_break(f.readline())
    
    return page_numbers
    

def print_queue_part1(file):
    """
    Print Queue part one

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0
    page_numbers=fill_page_numbers(file)
    
    print(page_numbers)

    f=open(file, "r")
    line=f.readline()
    while(line != '\n'):
        line=f.readline()
    
    line=remove_line_break(f.readline())
    while (line != ''):
        orders=line.split(',')
        print(orders)
        for page in orders:
            is_good=True
            for i in page_numbers[page]:
                
                page1 = next(obj for obj in orders if obj == page)
                print(page1)
                page2 = next(obj for obj in orders if obj == i)
                print(page2)
            
                if page1 > page2:
                    is_good=False
                    
            if (is_good):
                middle_page=orders.index(math.floor(len(orders/2)))
                count+=middle_page
        
        line=remove_line_break(f.readline())
        
    return count

def main():
    print('# Day 05 - part 1')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(print_queue_part1(arg1)))

if __name__=="__main__":
    main()