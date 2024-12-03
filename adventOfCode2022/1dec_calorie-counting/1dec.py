def lutin_max_calories(file):
    """
    """
    f = open(file, "r")
    calories_tmp=0
    list_lutins=[]
    line=f.readline()
    while (line != ''):
        if(line=='\n'):
            list_lutins.append(calories_tmp)
            calories_tmp=0
        else:
            calories_tmp+=int(line)
        line=f.readline()
    return max(list_lutins)

def three_first_lutins(liste):
    """
    """
    liste=sorted(liste,reverse=True)
    return sum(liste[0:3])
    
    
    
    
