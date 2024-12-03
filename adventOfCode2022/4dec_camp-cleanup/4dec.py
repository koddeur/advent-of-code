def ranges(file):
    """
    """
    f = open(file, "r")
    nb_ranges=0
    line=f.readline()
    while(line != ''):
        pairs=line.split(',')
        pair1=pairs[0]
        pair2=pairs[1][:-1]
        p1m1 = int(pair1.split('-')[0])
        p1m2 = int(pair1.split('-')[1])
        p2m1 = int(pair2.split('-')[0])
        p2m2 = int(pair2.split('-')[1])
        if(p1m1 >= p2m1 and p1m2 <= p2m2):
            nb_ranges+=1
        elif(p2m1 >= p1m1 and p2m2 <= p1m2):
            nb_ranges+=1
        line=f.readline()
    return nb_ranges

def ranges_2(file):
    """
    """
    f = open(file, "r")
    nb_ranges=0
    line=f.readline()
    while(line != ''):
        pairs=line.split(',')
        pair1=pairs[0]
        pair2=pairs[1][:-1]
        p1m1 = int(pair1.split('-')[0])
        p1m2 = int(pair1.split('-')[1])
        p2m1 = int(pair2.split('-')[0])
        p2m2 = int(pair2.split('-')[1])
        if(p1m1 <= p2m1 and p1m2 >= p2m1):
            nb_ranges+=1
        elif(p2m1 <= p1m1 and p2m2 >= p1m1):
            nb_ranges+=1
        line=f.readline()
    return nb_ranges
