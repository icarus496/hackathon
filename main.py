import pygame
import sys
screen_dimensions = [600,600]
screen=pygame.display.set_mode(screen_dimensions)
screencolor=(100,200,255)
screen.fill(screencolor)
def main(rectlist):
    save=pygame.Rect(0,0,50,25)
    tracelist=[]
    saved=False
    screen.fill(screencolor)
    m=0
    while True:
        mousex = pygame.mouse.get_pos()[0]
        mousey = pygame.mouse.get_pos()[1]

        if pygame.mouse.get_pressed()[0] and m>=150:
            if (mousex in range(50) and mousey in range(25)):
                n=[rectlist,tracelist]
                return n
            elif not saved:
                tracelist.append(pygame.Rect(mousex, mousey, 10, 10))
                print pygame.Rect(mousex, mousey, 10, 10)


        #Drawing rectangle
        pygame.draw.rect(screen, (255, 0, 0), save)
        for item in range(len(rectlist)):
            pygame.draw.rect(screen, (0, 0, 0), rectlist[item])
        for item in range(len(tracelist)):
            pygame.draw.rect(screen, (255, 255, 255), tracelist[item])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        m+=1
