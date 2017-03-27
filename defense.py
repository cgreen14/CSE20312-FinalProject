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
dhoz = 0
dvert = 0
crashed = False
while not crashed:
	for event in pygame.event.get():  #next week work to update this to take into account pressed keys
									# may need to re-format the get structure
		if event.type == pygame.QUIT:
			crashed = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				dhoz -= 10
			elif event.key == pygame.K_RIGHT:
				dhoz += 10
			elif event.key == pygame.K_UP:
				dvert -= 10
			elif event.key == pygame.K_DOWN:
				dvert += 10
# could possibly due mouse clicks to buttons here, to have player build into
#board

	gameDisplay.fill(green)
# this would be the place to check for valid tank movement, would need to check
# before making the change then revert
	tankDraw(x+dhoz,y+dvert)
	pygame.display.update()
	clock.tick(FPS)


pygame.quit()
