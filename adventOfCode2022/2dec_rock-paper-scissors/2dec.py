# -- PART 1

# A pierre (1)
# B papier (2)
# C ciseaux (3)

# X pierre (1)
# Y papier (2)
# Z ciseaux (3)

# -- PART 2

# X défaite
# Y nul
# Z victoire

def rock_paper_scissors(strat):
    """
    """
    f = open(strat, "r")
    scoreB=0
    line=f.readline()
    while(line != ''):
        playA = line[0]
        playB = line[2]
        #print(playA,playB)
        scoreB += scorePlay(playB)
        scoreB += scoreGame(playA,playB)  
        line=f.readline()
    return scoreB

def rock_paper_scissors_2(strat):
    """
    """
    f = open(strat, "r")
    scoreB=0
    line=f.readline()
    while(line != ''):
        playA = line[0]
        resultat = line[2]
        playB = resultatGame(playA,resultat)
        # print(playA,playB)
        scoreB += scorePlay(playB)
        scoreB += scoreGame(playA,playB)  
        line=f.readline()
    return scoreB

def resultatGame(playA, resultat):
    """
    """
    if (resultat == 'X'):
        if (playA == 'A') :
            return 'Z'
        elif (playA == 'B'):
            return 'X'
        elif (playA == 'C'):
            return 'Y'
    elif (resultat == 'Y'):
        if (playA == 'A') :
            return 'X'
        elif (playA == 'B'):
            return 'Y'
        elif (playA == 'C'):
            return 'Z'
    elif (resultat == 'Z'):
        if (playA == 'A') :
            return 'Y'
        elif (playA == 'B'):
            return 'Z'
        elif (playA == 'C'):
            return 'X'

def scorePlay(play):
    """
    """
    if (play == 'A' or play == 'X'):
        return 1
    elif (play == 'B' or play == 'Y'):
        return 2
    else :
        return 3

def scoreGame(playA,playB):
    """
    """
    if game(playA,playB) == -1 : # victoire
        return 6
    elif game(playA,playB) == 1 : # defaite
        return 0
    else : # match nul
        return 3

def game(playA,playB):
    """
    """
    if (playA == 'A') :
        if (playB == 'X') :
            return 0
        elif (playB == 'Y') :
            return -1
        else :
            return 1
    elif (playA == 'B') :
        if (playB == 'X') :
            return 1
        elif (playB == 'Y'):
            return 0
        else :
            return -1
    elif (playA == 'C') :
        if (playB == 'X'):
            return -1
        elif (playB == 'Y'):
            return 1
        else :
            return 0
    
    
