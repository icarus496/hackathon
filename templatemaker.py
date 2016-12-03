#imports
import pygame
import sys
#init pygame
pygame.init()
#setting up the screen
screen_size = [1000,1000]
screen = pygame.display.set_mode(screen_size)
screencolor = (100,200,255)
background = pygame.Rect(0,0,1000,1000)
#main template writing function
def template():
    rectlist=[] #list of rect objects
    while True:
        pygame.draw.rect(screen,screencolor,background) #screen background
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

template()