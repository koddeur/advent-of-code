#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def binary_diagnostic_part2(file):
    """
    Binary diagnostic part two

    Args:
        file (String): the input file name

    Returns:
        int: the result
    """
    count=0
    oxygen_generator=""
    co2_scrubber=""

    f = open(file, "r")
    line=f.readline().replace("\n","")
    bits_counter=len(line)
    
    f.seek(0)
    values_oxygen = [val.replace("\n","") for val in f.readlines()]
    f.seek(0)
    values_co2 = [val.replace("\n","") for val in f.readlines()]
    
    for bit_index in range(bits_counter):
        bit_counter_oxygen={"1":0,"0":0}
        bit_counter_co2={"0":0,"1":0}
            
        for value_oxygen in values_oxygen :
            bit_counter_oxygen[value_oxygen[bit_index]]+=1
            
        for valeur in values_co2 :
            bit_counter_co2[valeur[bit_index]]+=1
        
        max_common_bit = max(bit_counter_oxygen, key=bit_counter_oxygen.get)
        min_common_bit = min(bit_counter_co2, key=bit_counter_co2.get)
        
        remain_oxygen_values=[v for v in values_oxygen if v[bit_index]==max_common_bit]
        remain_co2_values=[v for v in values_co2 if v[bit_index]==min_common_bit]
        
        if (len(remain_oxygen_values)==1): # if only one value remain, keep this value
            oxygen_generator = remain_oxygen_values[0]
        if (len(remain_co2_values)==1): # if only one value remain, keep this value
            co2_scrubber = remain_co2_values[0]
        
        values_oxygen=remain_oxygen_values
        values_co2=remain_co2_values
    
    if (oxygen_generator == ""):
        oxygen_generator = remain_oxygen_values[0]
    if (co2_scrubber == ""):
        co2_scrubber = remain_co2_values[0]
    
    count = int(oxygen_generator, 2) * int(co2_scrubber, 2)

    return count

def main():
    print('# Day 03 - part 2')
    print('-----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(binary_diagnostic_part2(arg1)))

if __name__=="__main__":
    main()