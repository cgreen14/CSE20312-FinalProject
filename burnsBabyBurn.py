#!/usr/bin/env python2.7

##################
# Import Modules #
##################
import sys
import os
import time
import pygame

########################
# Initialize Variables #
########################
scrWidth = 800
scrHeight = 600
FPS = 30
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
gameContinue = True

##########################
# Images/Image Positions #
##########################
backgroundImg = pygame.image.load("level1Map.png")
backgroundImg = pygame.transform.scale(backgroundImg, (scrWidth, scrHeight))
backgroundImgRect = backgroundImg.get_rect()
tank1Img = pygame.image.load("tank1.png")
tank1Img = pygame.transform.scale(tank1Img, (tank1Img.get_width() / 3, tank1Img.get_height() / 3))
tank1Img = pygame.transform.rotate(tank1Img, -90)
tank2Img = pygame.image.load("tank2.png")
tank3Img = pygame.image.load("tank3.png")

###########
# Classes #
###########
class Tank(pygame.sprite.Sprite):
	def __init__(self, image):
		super(Tank, self).__init__()
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 310
		self.velX = 1
		self.velY = 0
		self.heath = 100
	def update(self):
		if (self.rect.x < 110):
			self.velX = 1
			self.velY = 0
		elif (self.rect.x < 150 and self.rect.y > 140):
			self.velX = 0;
			self.velY = -1;	
		elif (self.rect.x < 280 and self.rect.y > 130):
			self.velX = 1;
			self.velY = 0;	
		elif (self.rect.x < 300 and self.rect.y < 370):
			self.velX = 0;
			self.velY = 1;	
		elif (self.rect.x < 485 and self.rect.y < 490):
			self.velX = 1;
			self.velY = 0;	
		elif (self.rect.x < 500 and self.rect.y > 260):
			self.velX = 0;
			self.velY = -1;	
		elif (self.rect.y >= 260):
			self.velX = 1
			self.velY = 0
		self.rect.x += 10*self.velX
		self.rect.y += 10*self.velY

##########
# Groups #
##########
enemies = pygame.sprite.Group()

#############
# Test Case #
#############
enemy1 = Tank(tank1Img)
enemies.add(enemy1)

#################
# Initiate Game *
#################
pygame.init()
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((scrWidth, scrHeight))
print enemies.sprites()

while gameContinue:
	clock.tick(FPS)
	gameDisplay.blit(backgroundImg, backgroundImgRect)
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
			gameContinue = False
	enemies.update()
	enemies.draw(gameDisplay)
	pygame.display.update()

