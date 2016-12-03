#imports
import pygame
import sys
import time
#init pygame
pygame.init()
#setting up the screen
screen_size = [1000,1000]
screen = pygame.display.set_mode(screen_size)
screencolor = (100,200,255)
screen.fill(screencolor)
#main template writing function
def template():
    save=pygame.Rect(0,0,50,25)
    rectlist=[]                                                  #list of rect objects
    while True:

        #Allowing you to draw

        mousex = pygame.mouse.get_pos()[0]
        mousey = pygame.mouse.get_pos()[1]
        if pygame.mouse.get_pressed()[0]:
            rectlist.append(pygame.Rect(mousex, mousey, 10, 10))#append rectangles to list if mouse is pressed

        #Drawing everything should be under here

        for item in range(len(rectlist)):                       #looping through the rect list and drawing each rectangle in the list
            pygame.draw.rect(screen,(0, 0, 0), rectlist[item])   #same as above
        pygame.draw.rect(screen, (255, 0, 0), save)

        #checking input
        if mousex in range(50) and mousey in range(25):         #checking if mouse is on the save button
            if pygame.mouse.get_pressed()[0]:
                return rectlist
        for event in pygame.event.get():                        #making sure I can close the program
            if event.type==pygame.QUIT:
                sys.exit()
        pygame.display.update()                                 #update the screen