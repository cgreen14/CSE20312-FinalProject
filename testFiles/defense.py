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
FPS = 60
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
towerImg = pygame.transform.rotozoom(pygame.image.load('tower1.png'),0, 0.3)

def tankDraw(x,y):
	gameDisplay.blit(tankImg, (x,y))

def drawTower(x,y):
	gameDisplay.blit(towerImg, (x,y))

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
	else:
		x+=speed
	return x,y



#Main
x = scrWidth * 0.05
y = scrHeight * 0.52
dvert = 0
crashed = False
#Board set up


#Game start
end_it=False
while (end_it==False):
    gameDisplay.fill((0,0,0))
    myfont=pygame.font.SysFont("Britannic Bold", 40)
    nlabel=myfont.render("Welcome: Click 's' to begin", 1, (255, 0, 0))
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
			if event.key == pygame.K_s:
				end_it=True
    gameDisplay.blit(nlabel,(200,200))
    pygame.display.flip()
	#keep in bounds

gameDisplay.fill((0,0,0))
myfont=pygame.font.SysFont("Britannic Bold", 40)
nlabel=myfont.render("Welcome: Click 'b' to start setting up the map", 1, (255, 0, 0))
gameDisplay.blit(nlabel,(75,200))
pygame.display.flip()
quit = True
while(quit):
	for event in pygame.event.get():  #next week work to update this to take into account pressed keys
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				quit = False
			if event.key == pygame.K_b:
					gameDisplay.fill((0, 0, 0))
					gameDisplay.blit(level1Map, level1MapRect)
					pygame.display.update()
					clock.tick(FPS)
					pygame.display.flip()

			if event.key == pygame.K_s:
				count = 0
				while(count < 100):
					x,y = runAlongTrack(x,y)
					gameDisplay.fill((0, 0, 0))
					gameDisplay.blit(level1Map, level1MapRect)
					
					tankDraw(x,y)
					drawTower(40,80)
					pygame.display.update()
					clock.tick(FPS)
					pygame.display.flip()
					count += 1

pygame.quit()
