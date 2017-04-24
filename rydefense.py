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
red = (255, 0, 0)
white = (255,255,255)
black = (0,0,0)

#Set Up Pygame window
pygame.init()
pygame.display.set_caption('Tower Defense')
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((scrWidth, scrHeight))
level1Map = pygame.image.load("level1Map.png")
level1Map = pygame.transform.scale(level1Map, (scrWidth, scrHeight))
level1MapRect = level1Map.get_rect()
#Set Up Object to Move, we are inserting the image, fliping it and resizing it
tankImg = pygame.transform.rotozoom(pygame.image.load('tank1.png'),270, 0.25)
towerImg = pygame.transform.rotozoom(pygame.image.load('tower.png'),0, 0.3)
#text
myfont = pygame.font.SysFont("Britannic Bold", 40)
myfont2 = pygame.font.SysFont("Britannic Bold", 20)
nlabel= myfont.render("Welcome to Tower Defense", 1, red)
nlabelp = myfont.render("Play", 1, black)
nlabellead = myfont.render("Leaders", 1, black)
nlabeltower = myfont2.render("New Tower", 1, black)
nlabeltowerc = myfont2.render("Cost: 200", 1, black)


def runAlongTrack(x,y):
	speed = 10
	#rotation
	if(x < 110):
		x += speed
	elif(x < 150 and y > 140):
		y-= speed
	elif(y>130 and x < 280):
		x+=speed
	elif(x<300 and y < 370 ):
		y+=speed
	elif(y < 400 and x < 490):
		x+=speed
	elif(x < 500 and y > 260):
		y-=speed
	else:
		x+=speed
	return x,y

def tankDraw(x,y, tankImg):
	if(x == 110):
		tankImg = pygame.transform.rotate(tankImg, 90)
	if(x == 280):
		tankImg = pygame.transform.rotate(tankImg, -90)
	if(x == 490):
		tankImg = pygame.transform.rotate(tankImg, 90)
	gameDisplay.blit(tankImg, (x,y))



#Main
x = scrWidth * 0.05
y = scrHeight * 0.52
dvert = 0
crashed = False
#Board set up


#Game start
end_start=False
gameQuit = False
while not end_start:
	gameDisplay.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
			end_start=True
			gameQuit = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_s:
				end_start=True
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			(pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
			#check for leaderboard
			if leaderbutton.collidepoint(pos) and pressed1 == 1:
				end_start = True
			#go to play
			if playbutton.collidepoint(pos) and pressed1 == 1:
				end_start = True
	leaderbutton = pygame.draw.rect(gameDisplay, white, [scrWidth*0.32, scrHeight*0.6, scrWidth*0.15, scrHeight*0.075])
	playbutton = pygame.draw.rect(gameDisplay, green, [scrWidth*0.52, scrHeight*0.6, scrWidth*0.15, scrHeight*0.075])
	gameDisplay.blit(nlabel, (scrWidth*0.26, scrHeight*0.33))
	gameDisplay.blit(nlabellead, (scrWidth*0.325, scrHeight*0.62))
	gameDisplay.blit(nlabelp, (scrWidth*0.56, scrHeight*0.62))
	pygame.display.flip()

#main game
xs = scrWidth * 0.05
ys = scrHeight * 0.52
while not gameQuit:
	for event in pygame.event.get():  #next week work to update this to take into account pressed keys
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
			gameQuit = True
		if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
			xs, ys = runAlongTrack(xs, ys)

	gameDisplay.blit(level1Map, level1MapRect)
	towerbutton = pygame.draw.rect(gameDisplay, white, [scrWidth*0.85, scrHeight*0.9, scrWidth*0.1, scrHeight*0.075])
	gameDisplay.blit(nlabeltower, (scrWidth*0.86, scrHeight*0.91))
	gameDisplay.blit(nlabeltowerc, (scrWidth*0.86, scrHeight*0.94))
	tankDraw(xs,ys, tankImg)
	pygame.display.update()
	clock.tick(FPS)
	pygame.display.flip()


pygame.quit()
