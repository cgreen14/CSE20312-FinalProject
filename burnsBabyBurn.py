#!/usr/bin/env python2.7


##################
# Import Modules #
##################
import sys
import os
import time
import math
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
# Start up window
pygame.init()
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((scrWidth, scrHeight))

#################
# Images/Labels #
#################
# Images/Labels
backgroundImg = pygame.image.load("level1Map.png")
towerBoardImg = pygame.image.load("towerBoard.png")
tank1Img = pygame.image.load("tank1.png")
tank2Img = pygame.image.load("tank2.png")
tank3Img = pygame.image.load("tank3.png")
baseImg = pygame.image.load("base1.png")
tower1Img = pygame.image.load("tower1.png")
myFont = pygame.font.SysFont("Britannic Bold", 30)
# Transformation
backgroundImg = pygame.transform.scale(backgroundImg, (scrWidth, scrHeight))
backgroundImgRect = backgroundImg.get_rect()
towerBoardImg = pygame.transform.scale(towerBoardImg, (towerBoardImg.get_width() / 3, towerBoardImg.get_height() / 3))
towerBoardImgRect = towerBoardImg.get_rect()
towerBoardImgRect.bottom = scrHeight
towerBoardImgRect.right = scrWidth
towerBoardInstructions1 = myFont.render("Click to select tower", 1, black)
towerBoardInstructions2 = myFont.render("Click again to drop", 1, black)
tank1Img = pygame.transform.scale(tank1Img, (tank1Img.get_width() / 3, tank1Img.get_height() / 3))
tank1Img = pygame.transform.rotate(tank1Img, -90)
tank2Img = pygame.transform.scale(tank2Img, (tank2Img.get_width() / 3, tank2Img.get_height() / 3))
tank2Img = pygame.transform.rotate(tank2Img, -90)
baseImg = pygame.transform.scale(baseImg, (baseImg.get_width() / 4, baseImg.get_height() / 4))
tower1Img = pygame.transform.scale(tower1Img, (tower1Img.get_width() / 9, tower1Img.get_height() / 9))
tower1ImgRect = tower1Img.get_rect()
tower1ImgRect.x = 590
tower1ImgRect.y = 500
tower1Cost = myFont.render("$200", 1, red)


###########
# Classes #
###########
class Money(pygame.sprite.Sprite):
	def __init__(self):
		super(Money, self).__init__()
		self.cash = 500
		self.myfont = pygame.font.SysFont("Britannic Bold", 60)
		self.image = self.myfont.render("${}".format(str(self.cash)), 1, black)
		self.rect = self.image.get_rect()
		self.rect.x = 170
		self.rect.y = 510
	def update(self):
		money.clear(gameDisplay, backgroundImg)
		self.image = self.myfont.render("${}".format(str(self.cash)), 1, black)
		self.rect = self.image.get_rect()
		self.rect.x = 170
		self.rect.y = 510
	def decrementCash(self, intNum):
		self.cash -= intNum
	def incrementCash(self, intNum):
		self.cash += intNum


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
		self.rect.x += self.velX
		self.rect.y += self.velY
		if self.health <= 0:
			enemies.clear(gameDisplay, backgroundImg)
			self.kill()
		else:
			pygame.draw.line(gameDisplay, red, (self.rect.x, self.rect.y), \
				(self.rect.x + self.health * .3, self.rect.y), 2)
	def damage(self, hitNum):
		self.health -= hitNum
	def hitBase(self):
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
		pygame.draw.line(gameDisplay, red, (self.rect.x + 2, self.rect.bottom - 2), \
			((self.rect.x + self.health * .56), self.rect.bottom - 2), 2)
		if self.health <= 0:
			bases.clear(gameDisplay, backgroundImg)
			self.kill()
	def damage(self, hitNum):
		self.health -= hitNum
		self.update()


class Tower(pygame.sprite.Sprite):
	def __init__(self, image, (xpos, ypos)):
		super(Tower, self).__init__()
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = xpos
		self.rect.y = ypos
		self.attackRange = 100
		self.target = None
		self.closestTargetRange = 800
		self.coolDown = time.time()
	def update(self):
		if self.target is None: self.coolDown = time.time()
		self.spotEnemy()
		if time.time() - self.coolDown > .5:
			self.coolDown = time.time()
			self.attackEnemy()
	def spotEnemy(self):
		self.target = None
		for enemy in enemies.sprites():
			distance = math.sqrt((self.rect.centerx - enemy.rect.x)**2 + (self.rect.bottom - enemy.rect.y)**2)
			if distance <= self.attackRange and distance < self.closestTargetRange:
				self.target = enemy
				self.closestTargetRange = distance
		self.closestTargetRange = 800
	def attackEnemy(self):
		if self.target is not None:
			self.target.damage(30)


##########
# Groups #
##########
enemies = pygame.sprite.Group()
bases = pygame.sprite.Group()
towers = pygame.sprite.Group()
money = pygame.sprite.Group()


#################
# Initiate Game *
#################

gameDisplay.blit(backgroundImg, backgroundImgRect)
gameDisplay.blit(towerBoardImg, towerBoardImgRect)
gameDisplay.blit(towerBoardInstructions1, (580, 450))
gameDisplay.blit(towerBoardInstructions2, (590, 470))
gameDisplay.blit(tower1Img, tower1ImgRect)
gameDisplay.blit(tower1Cost, (580, 580))
bases.add(Base())
myMoney = Money()
money.add(myMoney)
money.draw(gameDisplay)


#############
# Functions #
#############
def placeTower(towerImage):
	towerPlaced = False
	while not towerPlaced:
		event = pygame.event.wait()
		if event.type == pygame.MOUSEBUTTONDOWN:
			mousePosition = pygame.mouse.get_pos()
			if myMoney.cash >= 200:
				towers.add(Tower(towerImage, (mousePosition[0]-12, mousePosition[1]-65)))
				myMoney.decrementCash(200)
				money.update()
				money.draw(gameDisplay)
				towerPlaced = True
			else:
				towerPlaced = True


#############
# Play Game #
#############
while gameContinue:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameContinue = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				gameContinue = False
			if event.key == pygame.K_n:
				enemies.add(Tank(tank1Img))
			if event.key == pygame.K_d:
				myMoney.decrementCash(10)
				money.clear(gameDisplay, backgroundImg)
				money.update()
				money.draw(gameDisplay)
			if event.key == pygame.K_a:
				myMoney.incrementCash(10)
				money.clear(gameDisplay, backgroundImg)
				money.update()
				money.draw(gameDisplay)
		if event.type == pygame.MOUSEBUTTONDOWN:
				mousePosition = pygame.mouse.get_pos()
				if tower1ImgRect.collidepoint(mousePosition) == True:
					placeTower(tower1Img)
					
	# clear groups
	enemies.clear(gameDisplay, backgroundImg)
	bases.clear(gameDisplay, backgroundImg)
	towers.clear(gameDisplay, backgroundImg)
	# update groups
	towers.update()
	enemies.update()
	bases.update()
	# collision checks
	if len(bases.sprites()) > 0:
		collisionWithBase = pygame.sprite.spritecollideany(bases.sprites()[0], enemies)
		if collisionWithBase != None:
			bases.sprites()[0].damage(10)
			collisionWithBase.hitBase()
			if len(bases.sprites()) == 0:
				gameContinue = False
	# draw groups
	enemies.draw(gameDisplay)
	bases.draw(gameDisplay)
	towers.draw(gameDisplay)
	pygame.display.update()
