def marqueur(file):
    """
    """
    f = open(file, "r")
    i=0
    tampon=''
    dataFlow=f.readline()
    n=4
    while(i < len(dataFlow)):
        if(len(tampon)<n):
            tampon+=dataFlow[i]
        else:
            tampon=tampon[1:]+dataFlow[i]
        if(len(tampon)==n):
            existsTwoOccurences=False
            for car in tampon :
                if(tampon.count(car)>1):
                    existsTwoOccurences=True
            if(existsTwoOccurences==False):
                return i+1
        i+=1

def marqueur_2(file):
    """
    """
    f = open(file, "r")
    i=0
    tampon=''
    dataFlow=f.readline()
    n=14
    while(i < len(dataFlow)):
        if(len(tampon)<n):
            tampon+=dataFlow[i]
        else:
            tampon=tampon[1:]+dataFlow[i]
        if(len(tampon)==n):
            existsTwoOccurences=False
            for car in tampon :
                if(tampon.count(car)>1):
                    existsTwoOccurences=True
            if(existsTwoOccurences==False):
                return i+1
        i+=1

