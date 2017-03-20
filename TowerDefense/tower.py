#!/usr/bin/env Python2.7

import sys 
import os
# Import pygame and install it if the system doesnt already have it.
try:
	import pygame
except:
	os.system('pip install pygame')
	import pygame

# Initialize variables.
scrWidth = 800
scrHeight = 600
FPS = 30
green = (0,200,0)

# Set up the window.
pygame.init()
gameDisplay = pygame.display.set_mode((scrWidth,scrHeight))
pygame.display.set_caption('Tower Defense')
clock = pygame.time.Clock()

# Set up object to move, insert it, flip it, and resize it.
towerImg = pygame.transform.rotozoom(pygame.image.load('tower.png'),0, 0.3)

def drawTower(x,y):
	gameDisplay.blit(towerImg, (x,y))

x = scrWidth * 0.45
y = scrHeight * 0.05

# Main execution.
crashed = False
while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True

	gameDisplay.fill(green)
	drawTower(x,y)
	pygame.display.update()
	clock.tick(FPS)

pygame.quit()
