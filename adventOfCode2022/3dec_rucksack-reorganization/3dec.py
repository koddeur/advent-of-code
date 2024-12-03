def bag(bags):
    """
    """
    f = open(bags, "r")
    line=f.readline()
    priorities=priority()
    list_errors=[]
    while(line != ''):
        error=define_error(line)
        list_errors.append(priorities[error])
        line=f.readline()
    return sum(list_errors)

def bag_2(bags):
    """
    """
    f = open(bags, "r")
    line=f.readline()
    priorities=priority()
    bags=[]
    list_items=[]
    i=1
    while(line != ''):
        bags.append(line)
        if(i==3):
            item=get_common_item(bags)
            list_items.append(priorities[item])
            bags=[]
            i=0
        i+=1
        line=f.readline()
    return sum(list_items)

def get_common_item(bags):
    """
    """
    for item in bags[0] :
        if item in bags[1] and item in bags[2]:
            return item

def define_error(bag):
    """
    """
    mid = int((len(bag)-1)/2)
    part1 = bag[:mid]
    part2 = bag[mid:-1]
    for i in part1 :
        if i in part2 :
            return i
            #part2 = ''.join(c for c in part2 if c not in i)

def priority():
    """
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    index=1
    res={}
    for i in alphabet :
        res[i]=index
        index+=1
    for j in alphabet :
        res[j.upper()]=index
        index+=1
    return res

