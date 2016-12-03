import pygame
import sys
#import score
screen_dimensions = [600,600]
screen=pygame.display.set_mode(screen_dimensions)
screencolor=(100,200,255)
screen.fill(screencolor)
def tracing(rectlist):
    save=pygame.Rect(0,0,50,25) #early function definitions
    tracelist=[] #list of rects from the traced line
    screen.fill(screencolor)
    m=0 #timer, to fix a bug. It's there for a reason, trust me
    while True:
        mousex = pygame.mouse.get_pos()[0]
        mousey = pygame.mouse.get_pos()[1]

        if pygame.mouse.get_pressed()[0] and m>=150:
            if (mousex in range(50) and mousey in range(25)):
                n=[rectlist,tracelist] #stuff to return
                return n
            else:
                tracelist.append(pygame.Rect(mousex, mousey, 10, 10))


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
def main(rectlist):
    tracing_and_stencil=tracing(rectlist)
    stencil=tracing_and_stencil[0]
    trace=tracing_and_stencil[1]