#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def cafeteria_part2(file):
    """
    Cafeteria part two

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0

    f = open(file, "r")
    lines = f.read().split("\n\n")
    ranges = lines[0].split("\n")
    all_ranges=[]
    
    for id_range in ranges :
         
        id_range_min=int(id_range.split("-")[0])
        id_range_max=int(id_range.split("-")[1])
        
        new_range = [id_range_min,id_range_max]
        
        all_ranges.append(new_range)

    
    for elt in all_ranges :
        all_ranges = can_be_merge(elt,all_ranges)

    for ranges in all_ranges :
        count+=int(ranges[1])-int(ranges[0])+1

    return count

def can_be_merge(elt, allranges):
    for current in allranges:
        if current is elt:
            continue
        
        if is_mergeable(elt, current):
            merged = merge_ranges(elt, current)
            
            # Remove 2 old elements
            new_ranges = [r for r in allranges if r not in (elt, current)]
            new_ranges.append(merged)

            return can_be_merge(merged, new_ranges)

    return allranges

def is_same(first_range, second_range):
    if (first_range[0] == second_range[0] and first_range[1] == second_range[1]):
        return True
    return False

def is_mergeable(first_range, second_range):
    """Return True is the two ranges are mergeable

    Args:
        first_range (array): the first range
        second_range (array): the second range

    Returns:
        Boolean: return True if is mergeable, False otherwise
    """
    # case 1 : Le second est imprimé de façon inférieur au premier (ex [3,10] et [1,7] devient [1,10])
    if(second_range[0] <= first_range[0] and second_range[1] >= first_range[0] 
       and second_range[1] <= first_range[1] and second_range[1] >= first_range[0]):
        return True
    # case 2 : Le second est imbriqué de façon supérieur au premier (ex [3,10] et [4,13] devient [3,13])
    if(second_range[0] >= first_range[0] and second_range[0] <= first_range[1] 
       and second_range[1] >= first_range[0] and second_range[1] >= first_range[1]):
        return True
    # case 3 : Le second englobe tout le premier (ex [3,10] et [2,15] devient [2,15])
    if(second_range[0] <= first_range[0] and second_range[1] >= first_range[1]):
        return True
    return False
    

def merge_ranges(first_range, second_range):
    """
    """
    # case 1 : Le second est imprimé de façon inférieur au premier (ex [3,10] et [1,7] devient [1,10])
    if(second_range[0] <= first_range[0] and second_range[1] >= first_range[0] 
       and second_range[1] <= first_range[1] and second_range[1] >= first_range[0]):
        new_range_min=second_range[0]
        new_range_max=first_range[1]
        return [new_range_min,new_range_max]
    # case 2 : Le second est imbriqué de façon supérieur au premier (ex [3,10] et [4,13] devient [3,13])
    if(second_range[0] >= first_range[0] and second_range[0] <= first_range[1] 
       and second_range[1] >= first_range[0] and second_range[1] >= first_range[1]):
        new_range_min=first_range[0]
        new_range_max=second_range[1]
        return [new_range_min,new_range_max]
    # case 3 : Le second englobe tout le premier (ex [3,10] et [2,15] devient [2,15])
    if(second_range[0] <= first_range[0] and second_range[1] >= first_range[1]):
        return second_range
    
def main():
    print('# Day 05 - part 2')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(cafeteria_part2(arg1)))

if __name__=="__main__":
    main()