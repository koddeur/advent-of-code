import re

def stack(file):
    """
    """
    f = open(file, "r")

    stack1 = ['B','W','N']
    stack2 = ['L','Z','S','P','T','D','M','B']
    stack3 = ['Q', 'H', 'Z', 'W', 'R']
    stack4 = ['W','D','V','J','Z','R']
    stack5 = ['S','H','M','B']
    stack6 = ['L','G','N','J','H','V','B','P']
    stack7 = ['J','Q','Z','F','H','D','L','S']
    stack8 = ['W','S','F','J','G','Q','B']
    stack9 = ['Z','W','M','S','C','D','J']
    stacks = []
    stacks.append(stack1)
    stacks.append(stack2)
    stacks.append(stack3)
    stacks.append(stack4)
    stacks.append(stack5)
    stacks.append(stack6)
    stacks.append(stack7)
    stacks.append(stack8)
    stacks.append(stack9)

    res=''

    line=f.readline()
    while(line != ''):
        numbers = re.split('move | from | to |\n',line)[1:-1]
        fromStack = int(numbers[1])
        toStack = int(numbers[2])
        j=0
        while(j<int(numbers[0])):
            fromNb = stacks[fromStack-1].pop(-1)
            stacks[toStack-1].append(fromNb)
            j+=1
        line=f.readline()
    print(stacks)
    for stack in stacks:
        res+=stack[-1]
    return res

def stack_2(file):
    """
    """
    f = open(file, "r")

    stack1 = ['B','W','N']
    stack2 = ['L','Z','S','P','T','D','M','B']
    stack3 = ['Q', 'H', 'Z', 'W', 'R']
    stack4 = ['W','D','V','J','Z','R']
    stack5 = ['S','H','M','B']
    stack6 = ['L','G','N','J','H','V','B','P']
    stack7 = ['J','Q','Z','F','H','D','L','S']
    stack8 = ['W','S','F','J','G','Q','B']
    stack9 = ['Z','W','M','S','C','D','J']
    stacks = []
    stacks.append(stack1)
    stacks.append(stack2)
    stacks.append(stack3)
    stacks.append(stack4)
    stacks.append(stack5)
    stacks.append(stack6)
    stacks.append(stack7)
    stacks.append(stack8)
    stacks.append(stack9)

    res=''
    line=f.readline()
    while(line != ''):
        numbers = re.split('move | from | to |\n',line)[1:-1]
        fromStack = int(numbers[1])
        toStack = int(numbers[2])
        j=0
        tmp=[]
        while(j<int(numbers[0])):
            fromNb = stacks[fromStack-1].pop(-1)
            tmp.insert(0,fromNb)
            j+=1
        stacks[toStack-1] = stacks[toStack-1] + tmp
        line=f.readline()
    print(stacks)
    for stack in stacks:
        res+=stack[-1]
    return res
    
