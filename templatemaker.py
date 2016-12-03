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
    rectlist=[]                                                  #list of rect objects
    while True:
        mousex = pygame.mouse.get_pos()[0]
        mousey = pygame.mouse.get_pos()[1]
        if pygame.mouse.get_pressed()[0]:
            rectlist.append(pygame.Rect(mousex, mousey, 10, 10))#append rectangles to list if mouse is pressed
        for item in range(len(rectlist)):                       #looping through the rect list and drawing each rectangle in the list
            pygame.draw.rect(screen,(0, 0, 0),rectlist[item])   #same as above
        for event in pygame.event.get():                        #making sure I can close the program
            if event.type==pygame.QUIT:
                sys.exit()
        pygame.display.update()                                 #update the screen
        screen.fill(screencolor)
