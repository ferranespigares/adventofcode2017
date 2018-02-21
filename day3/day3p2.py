import math

def Step():
    global posX
    global posY
    global incX
    global incY
    posX+=incX
    posY+=incY

def CanTurnLeft():
    global Grid
    global posX
    global posY
    global Dir
    if Dir=="Right":
        if Grid[posX][posY-1]!=0:
            return False
        else:
            return True
    elif Dir=="Up":
        if Grid[posX-1][posY]!=0:
            return False
        else:
            return True
    elif Dir=="Left":
        if Grid[posX][posY+1]!=0:
            return False
        else:
            return True
    elif Dir=="Down":
        if Grid[posX+1][posY]!=0:
            return False
        else:
            return True

def TurnLeft():
    global Dir
    global incX
    global incY
    if Dir=="Right":
        Dir="Up"
        incX=0
        incY=-1
    elif Dir=="Up":
        Dir="Left"
        incX=-1
        incY=0
    elif Dir=="Left":
        Dir="Down"
        incX=0
        incY=1
    elif Dir=="Down":
        Dir="Right"
        incX=1
        incY=0

#Input
input=368078
#input=25
#Create grid of wxh squares
size=int(math.ceil(math.sqrt(input)))+1
w=size
h=size
Grid=[[0 for x in range(w)] for y in range(h)]
if size%2:
    originX=int(math.ceil(size/2.0))-1
    originY=originX
else:
    originX=int(size/2)-1
    originY=originX+1
#print size,originX,originY

Grid[originX][originY]=1
posX=originX
posY=originY

Dir="Right"
incX=1
incY=0

i=1
while i<input:
    i+=1
    Step()
    Grid[posX][posY]=Grid[posX-1][posY]+Grid[posX-1][posY-1]+Grid[posX][posY-1]+Grid[posX+1][posY-1]+Grid[posX+1][posY]+Grid[posX+1][posY+1]+Grid[posX][posY+1]+Grid[posX-1][posY+1]
    if Grid[posX][posY]>input:
        break
    if CanTurnLeft():
        TurnLeft()

print Grid[posX][posY]