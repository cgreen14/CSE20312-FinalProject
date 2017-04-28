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

##########
# Images #
##########
# Images
backgroundImg = pygame.image.load("level1Map.png")
tank1Img = pygame.image.load("tank1.png")
tank2Img = pygame.image.load("tank2.png")
tank3Img = pygame.image.load("tank3.png")
baseImg = pygame.image.load("base1.png")
# Transformation
backgroundImg = pygame.transform.scale(backgroundImg, (scrWidth, scrHeight))
backgroundImgRect = backgroundImg.get_rect()
tank1Img = pygame.transform.scale(tank1Img, (tank1Img.get_width() / 3, tank1Img.get_height() / 3))
tank1Img = pygame.transform.rotate(tank1Img, -90)
tank2Img = pygame.transform.scale(tank2Img, (tank2Img.get_width() / 3, tank2Img.get_height() / 3))
tank2Img = pygame.transform.rotate(tank2Img, -90)
baseImg = pygame.transform.scale(baseImg, (baseImg.get_width() / 4, baseImg.get_height() / 4))

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
		self.health = 100
		self.angle = 0
	def update(self):
		if self.rect.x < 110:
			self.velX = 1
			self.velY = 0
		elif self.rect.x < 150 and self.rect.y > 140:
			self.velX = 0
			self.velY = -1	
			if self.angle is not 90:
				self.image = pygame.transform.rotate(self.image, 90)
				self.angle = 90
		elif self.rect.x < 280 and self.rect.y > 130:
			self.velX = 1
			self.velY = 0	
			if self.angle is not 0:
				self.image = pygame.transform.rotate(self.image, -90)
				self.angle = 0
		elif self.rect.x < 300 and self.rect.y < 370:
			self.velX = 0
			self.velY = 1	
			if self.angle is not -90:
				self.image = pygame.transform.rotate(self.image, -90)
				self.angle = -90
		elif self.rect.x < 485 and self.rect.y < 490:
			self.velX = 1
			self.velY = 0	
			if self.angle is not 0:
				self.image = pygame.transform.rotate(self.image, 90)
				self.angle = 0
		elif self.rect.x < 500 and self.rect.y > 260:
			self.velX = 0
			self.velY = -1
			if self.angle is not 90:
				self.image = pygame.transform.rotate(self.image, 90)
				self.angle = 90
		elif self.rect.x < 810 and self.rect.y >= 260:
			self.velX = 1
			self.velY = 0
			if self.angle is not 0:
				self.image = pygame.transform.rotate(self.image, -90)
				self.angle = 0
		else:
			self.kill()
		self.rect.x += 5*self.velX
		self.rect.y += 5*self.velY
		pygame.draw.line(gameDisplay, red, (self.rect.x, self.rect.y), \
			(self.rect.x + self.health * .3, self.rect.y), 2)
		if self.health <= 0:
			enemies.clear(gameDisplay, backgroundImg)
			self.kill()

class Base(pygame.sprite.Sprite):
	def __init__(self):
		super(Base, self).__init__()
		self.image = baseImg
		self.rect = self.image.get_rect()
		self.rect.x = 735
		self.rect.y = 194
		self.health = 100
	def update(self):
		if self.health <= 0:
			bases.clear(gameDisplay, backgroundImg)
			self.kill()
		pygame.draw.line(gameDisplay, red, (self.rect.x + 2, self.rect.bottom - 2), \
			((self.rect.x + self.health * .6) - 2, self.rect.bottom - 2), 2)

class Tower(pygame.sprite.Sprite):
	def __init__(self):
		super(Base, self).__init__()


##########
# Groups #
##########
enemies = pygame.sprite.Group()
bases = pygame.sprite.Group()

#################
# Initiate Game *
#################
pygame.init()
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((scrWidth, scrHeight))
gameDisplay.blit(backgroundImg, backgroundImgRect)
baseTower = Base()
bases.add(baseTower)

#############
# Play Game #
#############
while gameContinue:
	clock.tick(FPS)
	print len(enemies.sprites())
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameContinue = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				gameContinue = False
			if event.key == pygame.K_n:
				enemies.add(Tank(tank1Img))
	enemies.clear(gameDisplay, backgroundImg)
	enemies.update()
	bases.clear(gameDisplay, backgroundImg)
	bases.update()
	enemies.draw(gameDisplay)
	bases.draw(gameDisplay)
	pygame.display.update()
	collisionWithBase = pygame.sprite.spritecollideany(baseTower, enemies)
	if collisionWithBase != None:
		baseTower.health -= 10
		bases.update()
		enemies.clear(gameDisplay, backgroundImg)
		enemies.draw(gameDisplay)
		collisionWithBase.kill()
		if len(bases.sprites()) == 0:
			gameContinue = False
