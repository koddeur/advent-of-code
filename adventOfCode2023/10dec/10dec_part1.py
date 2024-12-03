#!/usr/bin/env python3 
# author : Mael Avennec

import sys
from enum import Enum

board={}
startingPosition=(0,0)

class TileType(Enum):
    GROUND=('hello')
    VERTICAL_PIPE=('north','south')
    HORIZONTAL_PIPE=('west','east')
    BOTTOM_LEFT_BEND=('north','east')
    BOTTOM_RIGHT_BEND=('west','north')
    TOP_RIGHT_BEND=('west','south')
    TOP_LEFT_BEND=('south','east')

class Pipe :

    directions={'north':(0,-1), 'east': (1,0), 'south':(0,1), 'west':(-1,0)}
    opposite={'north':'south', 'east':'west', 'south':'north', 'west':'east'}

    def __init__(self, tile, xCoordinate, yCoordinate, tileType):
        self._tile=tile
        self._x=xCoordinate
        self._y=yCoordinate
        self._tileType=tileType
    
    def getTile(self):
        return self._tile
    
    def getType(self):
        """
        """
        return self._tileType
    
    def hasNeighbor(self):
        """
        """
        for cardinal in directions :
            xDir=directions[cardinal][0]
            yDir=directions[cardinal][1]

            if board[(self._x + xDir , self._y + yDir)] :
                return True
        return False
    
    def getFirstNeighbor(self):
        """
        """
        for cardinal in self.directions :
            xDir=self.directions[cardinal][0]
            yDir=self.directions[cardinal][1]

            nextTile = board[(self._x + xDir , self._y + yDir)]

            if (self.opposite[cardinal] in nextTile.getType().value) :
                return (self.opposite[cardinal],board[(self._x + xDir , self._y + yDir)])
    
    def getNextNeighbor(self, fromDirection):
        """
        """
        nextCardinal=[x for x in self._tileType.value if x!=fromDirection]
        nextCardinal=nextCardinal[0]
        xDir=self.directions[nextCardinal][0]
        yDir=self.directions[nextCardinal][1]

        return (self.opposite[nextCardinal], board[(self._x + xDir, self._y + yDir)])

        

def pipeMaze_partOne(file):
    """
    Pipe Maze enigma part one

    Args :
    file (str) -- the input file path
    
    Return :
    count (int) -- the farthest point from the startin position
    """
    global startingPosition
    global board
    count=1

    parse_input(file)
    
    nextVal = board[startingPosition].getFirstNeighbor()
    fromDir=nextVal[0]

    while(nextVal[1].getTile() != 'S'):
        nextVal=nextVal[1].getNextNeighbor(fromDir)
        fromDir=nextVal[0]
        
        count+=1

    return count//2

def parse_input(file_path):
    """
    """
    f = open(file_path, "r")
    line=f.readline()
    global board
    global startingPosition

    y=0
    while (line != '') : 
        line=line.replace('\n','')
        
        x=0
        while x<len(line):
            tileType = defineType(line[x])
            board[(x,y)]=Pipe(line[x],x,y,tileType)

            if (line[x]=='S') :
                startingPosition=(x,y)
            x+=1
        y+=1

        line = f.readline()
    f.close()

def defineType(tile):
    """
    """
    match tile :
        case '|' :
            return TileType.VERTICAL_PIPE
        case '-' :
            return TileType.HORIZONTAL_PIPE
        case 'L' :
            return TileType.BOTTOM_LEFT_BEND
        case 'J' :
            return TileType.BOTTOM_RIGHT_BEND
        case '7' :
            return TileType.TOP_RIGHT_BEND
        case 'F' :
            return TileType.TOP_LEFT_BEND
        case '.' :
            return TileType.GROUND


def main():
    arg1 = sys.argv[1]
    print('# Day 10 - part 1')
    print('-----------------')
    print('Result => {}'.format(pipeMaze_partOne(arg1)))

if __name__=="__main__":
    main()

