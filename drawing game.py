import pygame
import time
import sys
import main
import templatemaker
rect=pygame.Rect(300,120,400,175)       #sets params for play game button
rect2=pygame.Rect(300,450,400,175)      #sets params for analytics button
select1=pygame.Rect(225,95,525,250)     #sets params for on hover play button
select2=pygame.Rect(225,425,525,225)    #sets params for on hover analytics button
pygame.init()
screen_dimensions=[1000,1000]
screen=pygame.display.set_mode(screen_dimensions)
screencolor=(100,200,255) #sets background value
screen.fill(screencolor)
def write(str,location,font,color):
    myfont = font
    gmovr = myfont.render(str, 1, color)
    screen.blit(gmovr,location)
def menu():
    while True:
        mousex=(pygame.mouse.get_pos()[0])                   #return mouse position
        mousey=(pygame.mouse.get_pos()[1])
        opt1 = (mousex in range(300, 700) and mousey in range(120, 295)) #checks if mouse is in range of button 1
        opt2 = (mousex in range(300, 700) and mousey in range(450, 625)) #checks if mouse is in range of button 2
        if opt1==False:                                    #restores normal view (no hover)
            screen.fill((100,200,255))
        if opt2==False:
            screen.fill((100,200,255))
        if opt1==True:
            pygame.draw.rect(screen, (0,0,255), select1) #increases button size on hover
            if pygame.mouse.get_pressed()[0]:
                main.main(templatemaker.template())
        if opt2==True:
            pygame.draw.rect(screen, (0,0,255), select2)     #increases button2 size on hover
        pygame.draw.rect(screen, (0,0,255), rect)            #draws menu buttons
        pygame.draw.rect(screen,(0,0,255),rect2)
        write('PLAY GAME', [425, 195], pygame.font.Font(pygame.font.match_font('vgafix'), 40), (0, 255, 0))
        write('OPTIONS', [425, 525], pygame.font.Font(pygame.font.match_font('vgafix'), 40), (0, 255, 0))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        pygame.display.update()
menu()

