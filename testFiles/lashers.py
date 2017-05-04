#!/usr/bin/env Python2.7

#script to test the laser from tower to point on the map
import sys
import os
import time
import pygame
import math

#Initialize Variables
scrWidth = 800
scrHeight = 600
FPS = 60
green = (0,200,0)

#Set Up Pygame window
pygame.init()
pygame.display.set_caption('Laser from Tower')
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((scrWidth, scrHeight))

towerImg = pygame.transform.rotozoom(pygame.image.load('tower1.png'),0, 0.3)

def drawTower(x,y):
	gameDisplay.blit(towerImg, (x,y))

def lazzers(x1,y1,x2,y2):
    dY = abs(y1-y2)
    dX = abs(x1-x2)
    ratio = dY/dX
    nX = 
    while()
    pygame.draw.aaline(gameDisplay,(255,255,255),[x1,y1],[x2,y2],True)




x = scrWidth * 0.05
y = scrHeight * 0.52
end_it = False
while (end_it==False):
    drawTower(x,y)
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
			if event.key == pygame.K_s:
				end_it=True
    pygame.display.flip()
