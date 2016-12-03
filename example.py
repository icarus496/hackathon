Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 26 2016, 12:03:00) 
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> import pygame
>>> pygame.init()
(5, 1)
>>> import pygame
import random
import sys
from time import *
pygame.init()
screen_dimensions=[600,600]
global rectx
global running
rectx=0
screen = pygame.display.set_mode(screen_dimensions)
running=True
color = (255, 255, 255)
rect_color=(255,0,0)
def checkcollide(collideobj):
   rect = pygame.Rect(rectx, 590, 50, 10)
   global running
   if collideobj.bottom == rect.top:
       print 'yup'
       if ((collideobj.left in range(rect.left, rect.right) or (collideobj.right in range(rect.left, rect.right)))) or collideobj.left == rect.left or collideobj.right == rect.right:
           print "Game over"
           sys.exit()
def randomrects(amount):
   rects=[]
   for rect in range(amount):
       rectx=random.randint(0,550)
       recty=0
       rects.append(pygame.Rect(rectx,recty,50,50))
   return rects


def main():
   rectlist=randomrects(8)
   while running:
       global rectx
       global running
       keys = pygame.key.get_pressed()
       rect = pygame.Rect(rectx, 590, 50, 10)
       if rect.right != 600:
           if keys[pygame.K_d]:
               rectx += 10
       if rect.left != 0:
           if keys[pygame.K_a]:
               rectx -= 10
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
       print rect.left
       screen.fill(color)
       rect = pygame.Rect(rectx, 590, 50, 10)
       for randrect in rectlist:
           if randrect.top==600:
               rectlist=randomrects(8)
       for randrect in rectlist:
           pygame.draw.rect(screen,(0,255,0), randrect)
       pygame.draw.rect(screen, rect_color, rect)
       pygame.display.update()
       for randomrect in rectlist:
           checkcollide(randomrect)
       for randrect in rectlist:
           randrect.top+=15
       sleep(0.05)
main()
