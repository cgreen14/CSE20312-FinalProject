#!/usr/bin/env Python2.7

import sys
import os
import time
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
pygame.display.set_caption('Tower Defense')
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((scrWidth, scrHeight))
level1Map = pygame.image.load("level1Map.png")
level1Map = pygame.transform.scale(level1Map, (scrWidth, scrHeight))
level1MapRect = level1Map.get_rect()
#Set Up Object to Move, we are inserting the image, fliping it and resizing it
tankImg = pygame.transform.rotozoom(pygame.image.load('tank1.png'),270, 0.3)

def tankDraw(x,y):
	gameDisplay.blit(tankImg, (x,y))

x = scrWidth * 0.05
y = scrHeight * 0.52

def runAlongTrack(x,y):
	speed = 10
	if(x < 110):
		x += speed
	elif(x < 150 and y > 140):
		y-= speed
	elif(y>130 and x < 280):
		x+=speed
	elif(x<300 and y < 380 ):
		y+=speed
	elif(y < 400 and x < 490):
		x+=speed
	elif(x < 500 and y > 260):
		y-=speed
	elif(x < 760):
		x+=speed
	return x,y



#Main

dvert = 0
crashed = False
while (x > 0 and x<800 and y > 0 and y < 600):
	x,y = runAlongTrack(x,y)
	print x
	print y
#	dhoz += 1
	#keep in bounds
	for event in pygame.event.get():  #next week work to update this to take into account pressed keys
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x -= 10
			elif event.key == pygame.K_RIGHT:
				x += 10
			elif event.key == pygame.K_UP:
				y -= 10
			elif event.key == pygame.K_DOWN:
				y += 10
# could possibly due mouse clicks to buttons here, to have player build into
#board
			elif event.key == pygame.K_g:
				tankImg = pygame.transform.rotate(tankImg,rotate*90)

	gameDisplay.fill((0, 0, 0))
	gameDisplay.blit(level1Map, level1MapRect)
	# this would be the place to check for valid tank movement, would need to check
	# before making the change then revert
	tankDraw(x,y)
	pygame.display.update()
	clock.tick(FPS)
	pygame.display.flip()


pygame.quit()
