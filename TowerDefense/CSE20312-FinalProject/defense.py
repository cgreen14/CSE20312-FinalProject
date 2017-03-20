#!/usr/bin/env Python2.7

import sys 
import os
#import pygame and install it if the system doesnt have it
try:
	import pygame
except:
	os.system('pip install pygame')
	import pygame

#Initialize Variables
scrWidth = 800
scrHeight = 600
FPS = 30
green = (0,200,0)

#Set Up Pygame window
pygame.init()
gameDisplay = pygame.display.set_mode((scrWidth,scrHeight))
pygame.display.set_caption('Tower Defense')
clock = pygame.time.Clock()
#Set Up Object to Move, we are inserting the image, fliping it and resizing it
tankImg = pygame.transform.rotozoom(pygame.image.load('tank1.png'),180, 0.3)

def tankDraw(x,y):
	gameDisplay.blit(tankImg, (x,y))

x = scrWidth * 0.45
y = scrHeight * 0.05


#Main 
crashed = False
while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

	gameDisplay.fill(green)
	tankDraw(x,y)
	pygame.display.update()
	clock.tick(FPS)


pygame.quit()
