import pygame
import random
from time import *
global hero
global starting_enemies
import sys
import math
global nval
print pygame.__file__
nval=[1,12]
global starting_lvl

starting_lvl=1
#setting up the screen
pygame.init()
pygame.font.init()
screen_dimensions=[600,600]
screen=pygame.display.set_mode(screen_dimensions)
screen_color=(20,230,0)
hero=[300,300]
hero_rad=20
hero_color=(0,250,250)
enemycolor=(150,200,255)
enemyrad=20
starting_enemies=12
class Enemy:
    def __init__(self,startingpos,startingvelocity):
        self.v_direction=1 #Either 1 or -1
        self.velocity=startingvelocity
        self.position=startingpos
    def setv_direction(self,new):
        self.v_direction=new #Either 1 or -1
    def getposition(self):
        return self.position
    def set_velocity(self,newlocity):
        self.velocity[0]=newlocity[0]*self.v_direction
        self.velocity[1]=newlocity[1]*self.v_direction
    def set_pos(self,newpos):
        self.position[0]=newpos[0]
        self.position[1]=newpos[1]
    def update_position(self):
        if self.velocity[0] >= 10:
            self.set_velocity([3, self.velocity[1]])
        if self.velocity[1] >= 10:
            self.set_velocity([self.velocity[0], 3])
        if self.position[0]>580 or self.position[0]<20:
            self.set_velocity([(self.velocity[0]*-1)+random.randint(-5,5),self.velocity[1]])
        if self.position[1]>580 or self.position[1]<=20:
            self.set_velocity([self.velocity[0],(self.velocity[1]*-1)+random.randint(-5,5)])
        newpos=[self.velocity[0]+self.position[0],self.velocity[1]+self.position[1]]
        self.set_pos(newpos)
def write(str,location,font,color):
    myfont = font
    gmovr = myfont.render(str, 1, color)
    screen.blit(gmovr,location)
def main():
    global hero
    global swordpos
    global nval
    global invlcntr
    invlcntr=0
    enemlist=generate_enemies()
    swordstate=1
    #main game loop
    while True:
        swordstate1 = [hero[0], hero[1] + 60]
        swordstate2 = [hero[0] - 60, hero[1]]
        swordstate3 = [hero[0], hero[1] - 60]
        swordstate4 = [hero[0] + 60, hero[1]]
        if swordstate==1:
            swordpos=swordstate1
        if swordstate==2:
            swordpos=swordstate2
        if swordstate==3:
            swordpos=swordstate3
        if swordstate==4:
            swordpos=swordstate4
        screen.fill(screen_color)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        keysdown=pygame.key.get_pressed()
        if keysdown[pygame.K_q]:
            if swordstate==4:
                swordstate=1
            else:
                swordstate+=1
            sleep(0.03)
        if keysdown[pygame.K_e]:
            if swordstate==1:
                swordstate=4
            else:
                swordstate-=1
            sleep(0.03)
        if hero[1]!=20:
            if keysdown[pygame.K_w]:
                hero[1]-=10
        if keysdown[pygame.K_r]:
            sleep(1)
            hero=[300,300]
            main()
        if hero[1]!=580:
            if keysdown[pygame.K_s]:
                hero[1]+=10
        if hero[0]!=20:
            if keysdown[pygame.K_a]:
                hero[0]-=10
        if hero[0]!=580:
            if keysdown[pygame.K_d]:
                hero[0]+=10
        if checkcollision(enemlist)=='Dead':
            while True:
                gameover()
        for enemy in enemlist:
            if enemy!=None:
                enemy.update_position()
                pygame.draw.circle(screen,enemycolor,enemy.getposition(),enemyrad)
        pygame.draw.line(screen,hero_color,hero,swordpos)
        pygame.draw.circle(screen,hero_color,hero,hero_rad)
        write("Level:  "+str(nval[0]), [0, 10], pygame.font.Font(pygame.font.match_font('vgafix'), 15), (255, 0, 0))
        pygame.display.update()
        if invlcntr<=15:
            invlcntr+=1
        print invlcntr
        sleep(0.05)
def checkcollision(list):
    global starting_enemies
    global invlcntr
    for enemy in range(len(list)):
        enem=list[enemy]
        if enem!=None:
            if math.sqrt(((enem.position[0]-hero[0])**2)+((enem.position[1]-hero[1])**2))<=40:
                if invlcntr>15:
                    for enemy in range(len(list)):
                        list[enemy]=None
                    return 'Dead'
            if ((swordpos[0] in range(enem.position[0]-10 , enem.position[0]+10)) and (swordpos[1] in range(enem.position[1]-10,enem.position[1]+10)) or enem.position[0]>=600 or enem.position[0]<=0 or enem.position[1]>=600 or enem.position[1]<=0):
                list[enemy]=None
                starting_enemies-=1
                if starting_enemies==0:
                    nextlevel(True)
def generate_enemies():
    global starting_enemies
    enemlist=[]
    for enem in range(starting_enemies):
        enemlist.append(Enemy([random.randint(20,580),random.randint(20,580)],[random.randint(1,5),random.randint(1,5)]))
    return enemlist
def gameover():
    global starting_enemies
    global hero
    global invlcntr
    print invlcntr
    while True:
        myfont = pygame.font.SysFont("monospace", 15)
        gmovr = myfont.render("Game Over", 1, (255, 0, 0))
        restart=myfont.render("Press R to restart",1,(255,0,0))
        screen.blit(gmovr, (200, 300))
        screen.blit(restart,(200,350))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keysdown = pygame.key.get_pressed()
        if keysdown[pygame.K_r]:
            starting_enemies=nval[1]
            sleep(1)
            hero = [300, 300]
            main()
        pygame.display.update()
def nextlevel(ingame):
    global starting_enemies
    global nval
    nval[0]+=1
    nval[1]+=2
    print 'Yay'
    if ingame==True:
        myfont = pygame.font.SysFont("monospace", 15)
        gmovr = myfont.render("You have made it to the next level", 1, (0, 0, 255))
        restart = myfont.render("You have made it to level:  "+str(nval[0]), 1, (0, 0, 255))
        screen.blit(gmovr, (200, 300))
        screen.blit(restart, (200, 350))
        sleep(3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
    starting_enemies = nval[1]
    if ingame==False:
        sleep(0.5)
    if ingame==True:
        sleep(3)
    hero = [300, 300]
    if ingame==True:
        main()
def options():
    global nval
    screen.fill((0,0,0))
    while True:
        levelcounter=pygame.Rect(250,250,100,100)
        pygame.draw.rect(screen,(255,255,255),levelcounter)
        pygame.draw.circle(screen,(255,0,0),[300,550],50)
        write("Arrow keys to increase or decrease level",[0,100],pygame.font.Font(pygame.font.match_font('vgafix'),45),(0,255,0))
        write(str(nval[0]), [280, 270], pygame.font.Font(pygame.font.match_font('vgafix'), 100), (0, 255, 0))
        write("Back",[220,520],pygame.font.Font(pygame.font.match_font('vgafix'), 100),(100,0,255))
        keysdown=pygame.key.get_pressed()
        if (pygame.mouse.get_pressed()[0] == 1) and (pygame.mouse.get_pos()[0] in range(250, 350) and pygame.mouse.get_pos()[1] in range(500, 600)):
            menu()
        if keysdown[pygame.K_LEFT] and nval[0]!=1:
            nextlevel(False)
        if keysdown[pygame.K_RIGHT]:
            nextlevel(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
def menu():
    widthplay=100
    widthplay2=200
    while True:
        x=(pygame.mouse.get_pos()[0] in range(50,250) and pygame.mouse.get_pos()[1] in range(200,400))
        pos2=(pygame.mouse.get_pos()[0] in range(350,550) and pygame.mouse.get_pos()[1] in range(200,400))
        if x==True:
            pygame.draw.circle(screen, (0, 0, 255), [150, 300], widthplay2)
        elif x==False:
            screen.fill((0,0,0))
        if pos2==True:
            pygame.draw.circle(screen, (0, 0, 255), [450, 300], widthplay2)
        pygame.draw.circle(screen,(0,0,255),[150,300],widthplay)
        pygame.draw.circle(screen, (0, 0, 255), [450, 300], widthplay)
        write('PLAY GAME',[65,290],pygame.font.Font(pygame.font.match_font('vgafix'),40),(0,255,0))
        write('OPTIONS', [380, 290], pygame.font.Font(pygame.font.match_font('vgafix'), 40), (0, 255, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if (pygame.mouse.get_pressed()[0]==1) and (pygame.mouse.get_pos()[0] in range(50,250) and pygame.mouse.get_pos()[1] in range(200,400)):
            main()
        if (pygame.mouse.get_pressed()[0]==1) and (pygame.mouse.get_pos()[0] in range(400,500) and pygame.mouse.get_pos()[1] in range(250,350)):
            options()
        pygame.display.update()
menu()