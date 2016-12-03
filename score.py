import math
import pygame
score2=[]
dist2=[]
def score():
    scorepreavg=0
    for item in range(len(score2)):
        n=score2[item]
        scorepreavg=scorepreavg+n
    total=scorepreavg/len(score2)
    if total < 0:
        return 0
    return total
def adjust():
    for item in range(len(dist2)):
        n=dist2[item]
        n=100-n
        score2.append(n)
        score()
def calcDist(rect1,rect2):
    center=rect1.center
    center2=rect2.center
    x1=center[0]   #declares the params for each point
    y1=center[1]
    x2=center[0]
    y2=center[1]
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  #calculates distance between 2 mid points of rectangles
    dist2.append(dist)                                  #logs distance to dist2 array
    adjust()
def coltest():
    collide=pygame.Rect.colliderect()                   #checks if rect intersects with another rectangle
    if pygame.Rect.colliderect == True:
        score.append(100)                               #
    elif pygame.Rect.colliderect == False:
        calcDist()




