from array import *
import random
import copy 
import math


def newBoard():
        B= [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        return B


def zeroFromPos(pos, b):
        index = 0;
        for x in range(4):
                for y in range(4):
                        
                        if index == pos:
                                return {'x':x,'y':y}
                        else:   
                                if b[x][y] == 0:
                                        index+=1

def numZero(b) :
        index = 0
        for x in range(4):
                for y in range(4):
                        if b[x][y] == 0:
                                index+=1
        return index            
def addNewValue(b):
        r1 = random.randint(0,numZero(b))
        r2 = random.randint(1,3)
        if r2 == 3:
                r2 = 2
        pos = zeroFromPos(r1, b)
        x = pos['x']
        y = pos['y']
        b[x][y] = 2*r2
        



def shiftLeft(b):
        for x in range(4):
                for y in range(3,0,-1):
                        if b[x][y] == b[x][y-1]:
                                b[x][y-1] *=2
                                b[x][y] = 0
                        if b[x][y-1] == 0:
                                b[x][y-1] = b[x][y]
                                b[x][y] = 0
def shiftRight(b):
        for x in range(4):
                for y in range(0,3):
                        if b[x][y] == b[x][y+1]:
                                b[x][y+1] *=2
                                b[x][y] = 0
                        if b[x][y+1] == 0:
                                b[x][y+1] = b[x][y]
                                b[x][y] = 0
def shiftUp(b):
        for x in range(4):
                for y in range(3,0,-1):
                        if b[y][x] == b[y-1][x]:
                                b[y-1][x] *=2
                                b[y][x] = 0
                        if b[y-1][x] == 0:
                                b[y-1][x] = b[y][x]
                                b[y][x] = 0

def shiftDown(b):
        for x in range(4):
                for y in range(0,3):
                        if b[y][x] == b[y+1][x]:
                                b[y+1][x] *=2
                                b[y][x] = 0
                        if b[y+1][x] == 0:
                                b[y+1][x] = b[y][x]
                                b[y][x] = 0
def boardEquals(B1, B2):
        for x in range(4):
                for y in range(4):
                        if B1[x][y]!= B2[x][y]:
                                return 0
        return 1 



def doLeft(b):
        copyB = copy.deepcopy(b)
        shiftLeft(copyB)
        if boardEquals(b, copyB) == 0:
                for x in range(4):
                        for y in range(4):
                                b[x][y] = copyB[x][y]
                addNewValue(b)
        else:
                return 0 
def doRight(b):
        copyB = copy.deepcopy(b)
        shiftRight(copyB)
        if boardEquals(b, copyB) == 0:
                for x in range(4):
                        for y in range(4):
                                b[x][y] = copyB[x][y]
                addNewValue(b)
        else:
                return 0
def doUp(b):
        copyB = copy.deepcopy(b)
        shiftUp(copyB)
        if boardEquals(b, copyB) == 0:
                for x in range(4):
                        for y in range(4):
                                b[x][y] = copyB[x][y]
                addNewValue(b)
        else:
                return 0
def doDown(b):
        copyB = copy.deepcopy(b)
        shiftDown(copyB)
        if boardEquals(b, copyB) == 0:
                for x in range(4):
                        for y in range(4):
                                b[x][y] = copyB[x][y]
                addNewValue(b)
        else:
                return 0


def score(b):
        i = 0
        for x in range(4):
                for y in range(4):
                        if b[x][y] > 0:
                                binary = math.log(b[x][y]*.5)/math.log(2)
                                i+=b[x][y] * binary
        return i

def maxTile(b):
        i = 0
        for x in range(4):
                for y in range(4):
                        if b[x][y] > i:i = b[x][y]
        return i
def qMax(b):
        return maxTile(b) * 2
def reward():
        maxleftB = score(shiftLeft(copy.deepcopy(b)))
        maxrightB = score(shiftRight(copy.deepcopy(b)))
        maxdownB = score(shiftDown(copy.deepcopy(b)))
        maxupB = score(copy.deepcopy(b))
        
        maxScore = maxleftB
        state = "left"
        if maxScore < maxrightB:
                maxScore = maxrightB
                state = "right"
        if maxScore < maxdownB:
                maxScore = maxdownB
                state = "down"
        if maxScore < maxupB:
                maxScore = maxupB
                state = "up"
        
        return maxScore

#B=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,16]]
#B2=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,8]]
#print(doLeft(B))
#print(B)
#print(score(B))
#print(shiftLeft(B))
#print(maxTile(B))
#print(qMax(B2))



