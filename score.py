import math
import pygame
score2=[]
distlist=[]
global scoresum
scoresum=0
def score(rectlist1,rectlist2):
    global scoresum
    for item in range(len(rectlist1)):
        rect1=rectlist1[item]
        rect2=rectlist2[item]
        center=rect1.center
        center2=rect2.center
        x1=float(center[0])   #declares the params for each point
        y1=float(center[1])
        x2=float(center2[0])
        y2=float(center2[1])
        dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) #calculates distance between 2 mid points of rectangles
        distlist.append(dist)      #logs distance to dist2 array
    for item in range(len(distlist)):
        score2.append(100-distlist[item])
    for item in range(len(score2)):
        n=score2[item]
        scoresum=n+scoresum
    final_score=scoresum/len(score2)
    if final_score<0:
        final_score=0
    return final_score






