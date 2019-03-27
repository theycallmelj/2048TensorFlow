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
        r1 = random.randint(0,numZero(b)-1)
        
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
                        if b[x][y] > i:
                                i = b[x][y]
                                
        return i
def qMax(b):
        return maxTile(b) * 2
def qMultiply(par1, par2):
        return [par1 * par2, par1 * par2, par1 * par2, par1 * par2] 
def rewardMax(b):
        B1 = copy.deepcopy(b)
        B2 = copy.deepcopy(b)
        B3 = copy.deepcopy(b)
        B4 = copy.deepcopy(b)
        shiftLeft(B1)
        shiftRight(B2)
        shiftDown(B3)
        shiftUp(B4)
        maxleftB = score(B1)
        maxrightB = score(B2)
        maxdownB = score(B3)
        maxupB = score(B4)
        
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

def add(m1, m2):
        return [m1[0] + m2[0], m1[1] + m2[1], m1[2] + m2[2], m1[3] + m2[3]]
def reward(b):
        B1 = copy.deepcopy(b)
        B2 = copy.deepcopy(b)
        B3 = copy.deepcopy(b)
        B4 = copy.deepcopy(b)
        shiftLeft(B1)
        shiftRight(B2)
        shiftDown(B3)
        shiftUp(B4)
        maxleftB = score(B1)
        maxrightB = score(B2)
        maxdownB = score(B3)
        maxupB = score(B4)
        
        return [maxleftB, maxrightB, maxdownB, maxupB]

#B=newBoard()
#addNewValue(B)
#B2=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,8]]
#doLeft(B)
#print(B)
#print(B)
#print(score(B))
#print(shiftLeft(B))
#print(maxTile(B))
#print(qMax(B2))



