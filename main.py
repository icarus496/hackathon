import pygame
import sys
screen_dimensions = [600,600]
screen=pygame.display.set_mode(screen_dimensions)
screencolor=(100,200,255)
screen.fill(screencolor)
def main(rectlist):
    while True:
        screen.fill(screencolor)


        #Drawing rectangles
        for item in range(len(rectlist)):
            pygame.draw.rect(screen,(0,0,0),rectlist[item])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

