import pygame
import sys
import os
import score
pygame.init()
screen_dimensions=[1000,1000]
screen=pygame.display.set_mode(screen_dimensions)
screencolor=(100,200,255) #sets background value
screen.fill(screencolor)
def write(str, location, font, color):
        myfont = font
        gmovr = myfont.render(str, 1, color)
        screen.blit(gmovr, location)
def analytics():
    while True:

        #if os.path.exists("hackathon./userscores.txt"):
        f = open ("userscores.txt","r")
        lines = f.readlines()
        write('Highscores', [390, 80], pygame.font.Font(pygame.font.match_font('vgafix'), 60), (10, 21, 38))
        write(str(lines[0]),[250, 110], pygame.font.Font(pygame.font.match_font('vgafix'), 40), (10, 21, 38))
        #else
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()