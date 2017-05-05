#!/usr/bin/env python2.7

##################
# Import Modules #
##################
import sys
import os
import time
import math
import pygame
from random import randint


########################
# Initialize Variables #
########################
# Variables
fromleader = 0
scrWidth = 800
scrHeight = 600
FPS = 30
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (200, 200, 0)
orange = (255, 165 ,0 )
level = 1
towerSelected = False
colorlist = [green, blue, white, yellow, orange]
filen = 'board.txt'
ycords = [0.3, 0.4, 0.5, 0.6, 0.7]
# Start up window
pygame.init()
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((scrWidth, scrHeight))

#################
# Images/Labels #
#################
# Images/Labels
attackBallImg = pygame.image.load("attackBall.png")
backgroundImg = pygame.image.load("level1Map.png")
woodenBackImg = pygame.image.load("woodenback.png")
tank1Img = pygame.image.load("tank1.png")
tank2Img = pygame.image.load("tank2.png")
tank3Img = pygame.image.load("tank3.png")
baseImg = pygame.image.load("base1.png")
tower1Img = pygame.image.load("tower1.png")
tower3Img = pygame.image.load("tower3.png")
myFont = pygame.font.SysFont("Britannic Bold", 30)
levelFont = pygame.font.SysFont("Britannic Bold", 60)
namefont = pygame.font.SysFont("Britannic Bold", 25)
nlabel= levelFont.render("Welcome to Tower Defense", 1, red)
nlabelp = myFont.render("Play", 1, black)
nlabellead = myFont.render("Leaders", 1, black)
# Transformation
attackBallImg = pygame.transform.scale(attackBallImg, (attackBallImg.get_width() / 45, attackBallImg.get_height() / 45))
backgroundImg = pygame.transform.scale(backgroundImg, (scrWidth, scrHeight))
backgroundImgRect = backgroundImg.get_rect()
towerBoardInstructions1 = myFont.render("Click and hold to select tower", 1, black)
levelDisplay = levelFont.render("Level {}".format(level), 1, black)
nameLabel = myFont.render("User Number", 1, red)
scoreLabel = myFont.render("Max Level", 1, red)
labelltom = myFont.render("Home", 1, black)
exitLabel = myFont.render("GAME OVER", 1, white)
woodenBackImg = pygame.transform.scale(woodenBackImg, (scrWidth, scrHeight / 6))
woodenBackImgRect = woodenBackImg.get_rect()
woodenBackImgRect.bottom = scrHeight
tank1Img = pygame.transform.scale(tank1Img, (tank1Img.get_width() / 3, tank1Img.get_height() / 3))
tank1Img = pygame.transform.rotate(tank1Img, -90)
tank2Img = pygame.transform.scale(tank2Img, (tank2Img.get_width() / 3, tank2Img.get_height() / 3))
tank2Img = pygame.transform.rotate(tank2Img, -90)
tank3Img = pygame.transform.scale(tank3Img, (tank3Img.get_width() / 4, tank3Img.get_height() / 4))
tank3Img = pygame.transform.rotate(tank3Img, -90)
baseImg = pygame.transform.scale(baseImg, (baseImg.get_width() / 4, baseImg.get_height() / 4))
tower1Img = pygame.transform.scale(tower1Img, (tower1Img.get_width() / 9, tower1Img.get_height() / 9))
tower3Img = pygame.transform.scale(tower3Img, (tower3Img.get_width() / 2, tower3Img.get_height() / 2))
tower3ImgRect = tower3Img.get_rect()
tower3ImgRect.x = 655
tower3ImgRect.y = 508
tower1ImgRect = tower1Img.get_rect()
tower1ImgRect.x = 590
tower1ImgRect.y = 510
tower1Cost = myFont.render("$200", 1, black)
tower3Cost = myFont.render("$500", 1, black)


##########
# Groups #
##########
enemies = pygame.sprite.Group()
bases = pygame.sprite.Group()
towers = pygame.sprite.Group()
money = pygame.sprite.Group()
instructions = pygame.sprite.Group()
roundTimes = pygame.sprite.Group()
attacks = pygame.sprite.Group()


###########
# Classes #
###########
class singleBullet(pygame.sprite.Sprite):
	def __init__(self, xPos, yPos, target, bulletType):
		super(singleBullet, self).__init__()
		self.bulletType = bulletType
		self.image = attackBallImg
		self.xPos = xPos
		self.yPos = yPos
		self.rect = self.image.get_rect()
		self.rect.x = self.xPos
		self.rect.y = self.yPos
		self.target = target
		self.xVel = 7
		self.yVel = 7
	def update(self):
		if math.fabs(self.rect.centerx - self.target.rect.centerx) < 5 and \
			math.fabs(self.rect.centery - self.target.rect.centery) < 5:
			if self.bulletType == 1:
				self.target.damage(30)
			else:
				self.target.damage(80)
			attacks.clear(gameDisplay, backgroundImg)
			self.kill()
		if self.rect.centerx < self.target.rect.centerx:
			self.rect.centerx += self.xVel
		elif self.rect.centerx > self.target.rect.centerx:
			self.rect.centerx -= self.xVel
		if self.rect.centery < self.target.rect.centery:
			self.rect.centery += self.yVel
		elif self.rect.centery > self.target.rect.centery:
			self.rect.centery -= self.yVel


class TimeUntilRoundStarts(pygame.sprite.Sprite):
	def __init__(self, initialTime):
		super(TimeUntilRoundStarts, self).__init__()
		self.initialTime = initialTime
		self.myfont = pygame.font.SysFont("Britannic Bold", 40)
		self.image = self.myfont.render("0:{}".format(self.initialTime), 1, black)
		self.rect = self.image.get_rect()
		self.rect.x = 14
		self.rect.y = 470
	def update(self):
		roundTimes.clear(gameDisplay, backgroundImg)
		self.initialTime -= 1
		self.image = self.myfont.render("0:{}".format(self.initialTime), 1, black)
		roundTimes.draw(gameDisplay)
	def isTimeAtZero(self):
		if self.initialTime <= 0:
			self.initialTime = 15
			return True
		return False


class Instructions(pygame.sprite.Sprite):
	def __init__(self):
		super(Instructions, self).__init__()
		self.myfont = pygame.font.SysFont("Britannic Bold", 60)
		self.image = self.myfont.render("Good luck!", 1, black)
		self.rect = self.image.get_rect()
		self.rect.center = (370, 554)
	def dropInstructions(self, instructionsToPrint):
		self.instructionsToPrint = instructionsToPrint
		instructions.clear(gameDisplay, backgroundImg)
		money.clear(gameDisplay, backgroundImg)
		gameDisplay.blit(woodenBackImg, woodenBackImgRect)
		gameDisplay.blit(tower1Img, tower1ImgRect)
		gameDisplay.blit(tower3Img, tower3ImgRect)
		gameDisplay.blit(tower1Cost, (622, 540))
		gameDisplay.blit(tower3Cost, (730, 540))
		gameDisplay.blit(levelDisplay, (14, 510))
		self.image = self.myfont.render(self.instructionsToPrint, 1, black)
		self.rect = self.image.get_rect()
		self.rect.center = (370, 554)
		instructions.draw(gameDisplay)
		money.draw(gameDisplay)


class Money(pygame.sprite.Sprite):
	def __init__(self):
		super(Money, self).__init__()
		self.cash = 500
		self.myfont = pygame.font.SysFont("Britannic Bold", 60)
		self.image = self.myfont.render("${}".format(str(self.cash)), 1, black)
		self.rect = self.image.get_rect()
		self.rect.x = 30
		self.rect.y = 550
	def update(self):
		instructions.clear(gameDisplay, backgroundImg)
		money.clear(gameDisplay, backgroundImg)
		gameDisplay.blit(woodenBackImg, woodenBackImgRect)
		gameDisplay.blit(tower1Img, tower1ImgRect)
		gameDisplay.blit(tower3Img, tower3ImgRect)
		gameDisplay.blit(tower1Cost, (622, 540))
		gameDisplay.blit(tower3Cost, (730, 540))
		gameDisplay.blit(levelDisplay, (14, 510))
		self.image = self.myfont.render("${}".format(str(self.cash)), 1, black)
		instructions.draw(gameDisplay)
		money.draw(gameDisplay)
	def decrementCash(self, intNum):
		self.cash -= intNum
	def incrementCash(self, intNum):
		self.cash += intNum


class Tank(pygame.sprite.Sprite):
	def __init__(self, image, tankType, initialHealth):
		super(Tank, self).__init__()
		self.image = image
		self.initialHealth = initialHealth
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 310
		self.velX = 1
		self.velY = 0
		self.tankType = tankType
		self.health = self.initialHealth / (self.tankType)
		self.angle = 0
	def update(self):
		if self.rect.x < 110:
			self.velX = 1
			self.velY = 0
		elif self.rect.x > 112 and self.rect.x < 200 and self.rect.y > 140:
			self.velX = 0
			self.velY = -1
			if self.angle is not 90:
				self.image = pygame.transform.rotate(self.image, 90)
				self.angle = 90
		elif self.rect.x < 250 and self.rect.y < 135:
			self.velX = 1
			self.velY = 0
			if self.angle is not 0:
				self.image = pygame.transform.rotate(self.image, -90)
				self.angle = 0
		elif self.rect.x > 272 and self.rect.y < 140:
			self.velX = 0
			self.velY = 1
			if self.angle is not -90:
				self.image = pygame.transform.rotate(self.image, -90)
				self.angle = -90
		elif self.rect.x > 272 and self.rect.x < 300 and self.rect.y > 370:
			self.velX = 1
			self.velY = 0
			if self.angle is not 0:
				self.image = pygame.transform.rotate(self.image, 90)
				self.angle = 0
		elif self.rect.x > 488 and self.rect.y > 370:
			self.velX = 0
			self.velY = -1
			if self.angle is not 90:
				self.image = pygame.transform.rotate(self.image, 90)
				self.angle = 90
		elif self.rect.x > 488 and self.rect.x < 810 and self.rect.y < 257:
			self.velX = 1
			self.velY = 0
			if self.angle is not 0:
				self.image = pygame.transform.rotate(self.image, -90)
				self.angle = 0
		self.rect.x += self.tankType * self.velX
		self.rect.y += self.tankType * self.velY
		if self.health <= 0:
			enemies.clear(gameDisplay, backgroundImg)
			myMoney.incrementCash(25)
			money.update()
			money.draw(gameDisplay)
			self.kill()
		else:
			pygame.draw.line(gameDisplay, red, (self.rect.x, self.rect.y), \
				(self.rect.x + (self.health * 100 / self.initialHealth) * .3 * self.tankType, self.rect.y), 2)
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
		pygame.draw.line(gameDisplay, green, (self.rect.x + 2, self.rect.bottom - 2), \
			((self.rect.x + self.health * .56), self.rect.bottom - 2), 2)
		if self.health <= 0:
			bases.clear(gameDisplay, backgroundImg)
			self.kill()
	def damage(self, hitNum):
		self.health -= hitNum
		self.update()


class Tower(pygame.sprite.Sprite):
	def __init__(self, image, (xpos, ypos), towerType):
		super(Tower, self).__init__()
		self.towerType = towerType
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
		if time.time() - self.coolDown > 1:
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
			attacks.add(singleBullet(self.rect.left, self.rect.bottom, self.target, self.towerType))
			#self.target.damage(10)


######################
# Initialize Classes #
######################
instruction = Instructions()
levelTime = TimeUntilRoundStarts(15)
myMoney = Money()


#############
# Functions #
#############
def checkBounds(xpos, ypos):
	if (xpos > 0 and xpos < 160 and ypos > 300 and ypos < 356) \
		or (xpos > 98 and xpos < 165 and ypos > 122 and ypos < 356) \
		or (xpos > 109 and xpos < 315 and ypos > 121 and ypos < 179) \
		or (xpos > 269 and xpos < 317 and ypos > 121 and ypos < 418) \
		or (xpos > 270 and xpos < 532 and ypos > 364 and ypos < 419) \
		or (xpos > 482 and xpos < 534 and ypos > 241 and ypos < 417) \
		or (xpos > 482 and xpos < 797 and ypos > 242 and ypos < 301) \
		or (ypos > 500) \
		or (ypos < 70):
		return False
	return True

def spawnEnemy(initialHealth):
	tankType = randint(1, 3)
	if tankType == 1:
		enemies.add(Tank(tank1Img, tankType, initialHealth))
	elif tankType == 2:
		enemies.add(Tank(tank2Img, tankType, initialHealth))
	else:
		enemies.add(Tank(tank3Img, tankType, initialHealth))

#############
# Play Game #
#############
levelInProcess = False
startcontinue = True
leadercontinue = False
quitcontinue = False
maincontinue = False
gameContinue = True
#######################
# Set Up Leaderboarrd #
#######################
if not os.path.isfile(filen): #create file
	file = open(filen, "w+")
	for i in range(5):
		file.write("empty" + str(i) + ",0\n")
	file.close()
file = open(filen, "r")
usernumber = 0
for line in file:
	usernumber+=1
while gameContinue:
	while startcontinue:
		clock.tick(FPS)
		gameDisplay.fill((0,0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT or ( event.type == pygame.KEYDOWN and event.key == pygame.K_q ):
				startcontinue = False
				leadercontinue = False
				quitcontinue = False
				maincontinue = False
				gameContinue = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				(pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
				#check for leaderboard
				if leaderbutton.collidepoint(pos) and pressed1 == 1:
					startcontinue = False
					leadercontinue = True
					quitcontinue = False
					maincontinue = False
					gameContinue = True

				#go to play
				if playbutton.collidepoint(pos) and pressed1 == 1:
					startcontinue = False
					leadercontinue = False
					quitcontinue = False
					maincontinue = True
					gameContinue = True

		leaderbutton = pygame.draw.rect(gameDisplay, white, [scrWidth*0.32, scrHeight*0.6, scrWidth*0.15, scrHeight*0.075])
		playbutton = pygame.draw.rect(gameDisplay, green, [scrWidth*0.52, scrHeight*0.6, scrWidth*0.15, scrHeight*0.075])
		gameDisplay.blit(nlabel, (scrWidth*0.17, scrHeight*0.33))
		gameDisplay.blit(nlabellead, (scrWidth*0.35, scrHeight*0.62))
		gameDisplay.blit(nlabelp, (scrWidth*0.57, scrHeight*0.62))
		instuctionLabel = myFont.render("Player Number: " + str(usernumber - 4), 1, white)
		gameDisplay.blit(instuctionLabel, (scrWidth*0.385, scrHeight*0.5))
		pygame.display.flip()

	if maincontinue:
		#game set up, runs one time if maincontinue is hot
		bases.add(Base())
		money.add(myMoney)
		instructions.add(instruction)
		gameDisplay.blit(backgroundImg, backgroundImgRect)
		gameDisplay.blit(woodenBackImg, woodenBackImgRect)
		gameDisplay.blit(towerBoardInstructions1, (504, 470))
		gameDisplay.blit(tower1Img, tower1ImgRect)
		gameDisplay.blit(tower3Img, tower3ImgRect)
		gameDisplay.blit(tower1Cost, (622, 540))
		gameDisplay.blit(tower3Cost, (730, 540))
		gameDisplay.blit(levelDisplay, (14, 510))
		money.draw(gameDisplay)
		instructions.draw(gameDisplay)
		roundTimes.add(levelTime)
		enemiesLeftInLevel = 5
		enemiesPerLevel = 5
		initialEnemyHealth = 100
		enemySpawnTime = time.time()
		roundStartTime = time.time()
		roundTimes.draw(gameDisplay)
		levelDisplayDuration = time.time()
		whichTower = 0
	while maincontinue:
		clock.tick(FPS)
		if levelInProcess == False and time.time() - roundStartTime > 1:
			roundTimes.update()
			roundStartTime = time.time()
			if levelTime.isTimeAtZero():
				levelInProcess = True
				roundTimes.clear(gameDisplay, backgroundImg)
				instruction.dropInstructions("Level {} Started!".format(level))
				levelDisplayDuration = time.time()
				enemySpawnTime = time.time()

		# spawn enemies based on level
		if levelInProcess:
			if len(instruction.instructionsToPrint) > 0 and instruction.instructionsToPrint[0] == "L" \
				and time.time() - levelDisplayDuration > 4:
				instruction.dropInstructions("")
			if time.time() - enemySpawnTime > 1 and enemiesLeftInLevel > 0:
				enemySpawnTime = time.time()
				enemiesLeftInLevel -= 1
				spawnEnemy(initialEnemyHealth)
			if enemiesLeftInLevel == 0 and len(enemies.sprites()) == 0:
				instruction.dropInstructions("Level {} Finished!".format(level))
				level += 1
				roundStartTime = time.time()
				levelDisplay = levelFont.render("Level {}".format(level), 1, black)
				money.update()
				initialEnemyHealth += 50
				enemiesPerLevel += 3
				levelInProcess = False
				enemiesLeftInLevel = enemiesPerLevel

		# check for user input
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameContinue = False
				maincontinue = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					startcontinue = False
					leadercontinue = False
					quitcontinue = True
					maincontinue = False
					gameContinue = False
				if event.key == pygame.K_m:
					myMoney.decrementCash(200)
					money.update()
				if event.key == pygame.K_z:
					myMoney.incrementCash(200)
					money.update()
			# select tower
			if event.type == pygame.MOUSEBUTTONDOWN and towerSelected == False:
					mousePosition = pygame.mouse.get_pos()
					if tower1ImgRect.collidepoint(mousePosition) == True:
						towerSelected = True
						whichTower = 1
						instruction.dropInstructions("Release to place")
					if tower3ImgRect.collidepoint(mousePosition) == True:
						towerSelected = True
						whichTower = 3
						instruction.dropInstructions("Release to place")
			# place tower
			if event.type == pygame.MOUSEBUTTONUP and towerSelected:
					mousePosition = pygame.mouse.get_pos()
					if checkBounds(mousePosition[0], mousePosition[1]) and whichTower == 1 and myMoney.cash >= 200:
						towers.add(Tower(tower1Img, (mousePosition[0]-12, mousePosition[1]-65), 1))
						myMoney.decrementCash(200)
						money.update()
						money.draw(gameDisplay)
						instruction.dropInstructions("")
					elif checkBounds(mousePosition[0], mousePosition[1]) and whichTower == 3 and myMoney.cash >= 500:
						towers.add(Tower(tower3Img, (mousePosition[0]-50, mousePosition[1]-70), 3))
						myMoney.decrementCash(500)
						money.update()
						money.draw(gameDisplay)
						instruction.dropInstructions("")
					elif not checkBounds(mousePosition[0], mousePosition[1]):
						instruction.dropInstructions("Can't place there")
					else:
						instruction.dropInstructions("Out of cash")
					towerSelected = False
					whichTower = 0

		# clear groups
		attacks.clear(gameDisplay, backgroundImg)
		enemies.clear(gameDisplay, backgroundImg)
		bases.clear(gameDisplay, backgroundImg)
		towers.clear(gameDisplay, backgroundImg)

		# update groups
		attacks.update()
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
					startcontinue = False
					leadercontinue = False
					quitcontinue = True
					maincontinue = False
					gameContinue = False

		# draw groups
		attacks.draw(gameDisplay)
		enemies.draw(gameDisplay)
		bases.draw(gameDisplay)
		towers.draw(gameDisplay)
		pygame.display.update()
	while leadercontinue:
		clock.tick(FPS)
		#find if file exists, if not make one
		if not os.path.isfile(filen): #create file
			file = open(filen, "w+")
			for i in range(5):
				file.write("empty" + str(i) + ",0\n")
			file.close()

		file = open(filen, "r")

		#Display Top 5 Names
		scores = {}
		for line in file:
			name = line.split(",")[0].rstrip()
			if len(line.split(",")) > 1:
				score = line.split(",")[1].rstrip()
			scores[name] = score
		file.close()
		sortScore = sorted(scores, key=lambda x: int(scores[x]), reverse = True)
		leader = True
		while leader:
			gameDisplay.fill(black)
			gameDisplay.blit(nameLabel, (scrWidth*0.30, scrHeight*0.20))
			gameDisplay.blit(scoreLabel, (scrWidth*0.55, scrHeight*0.20))
			homebutton = pygame.draw.rect(gameDisplay, green, [scrWidth*0.40, scrHeight*0.8, scrWidth*0.15, scrHeight*0.075])
			gameDisplay.blit(labelltom, (scrWidth*0.44, scrHeight*0.823))
			for i,s in enumerate(sortScore):
				if i < 5:
					if scores[s] == "0":
						userLabel = namefont.render("XXX", 1, colorlist[i])
						gameDisplay.blit(userLabel, (scrWidth*0.31, scrHeight*ycords[i]))
						scoreL = namefont.render(scores[s], 1, colorlist[i])
						gameDisplay.blit(scoreL, (scrWidth*0.56, scrHeight*ycords[i]))
					else:
						userLabel = namefont.render(s, 1, colorlist[i])
						gameDisplay.blit(userLabel, (scrWidth*0.31, scrHeight*ycords[i]))
						scoreL = namefont.render(scores[s], 1, colorlist[i])
						gameDisplay.blit(scoreL, (scrWidth*0.56, scrHeight*ycords[i]))


			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
					leader = False
					startcontinue = False
					leadercontinue = False
					quitcontinue = False
					maincontinue = False
					gameContinue = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
					(pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
					#go back to home screen
					if homebutton.collidepoint(pos) and pressed1 == 1:
						leader = False
						startcontinue = True
						leadercontinue = False
						quitcontinue = False
						maincontinue = False
						gameContinue = True

	quitloop = 0
	while quitcontinue:
		clock.tick(FPS)
		if not os.path.isfile(filen): #create file
			file = open(filen, "w+")
			for i in range(5):
				file.write("empty" + str(i) + ",0\n")
			file.close()
		if quitloop == 0:
			file = open(filen, "a")
			file.write(str(usernumber - 4)+","+str(level)+"\n")
			file.close()
			quitloop = 1
		exitshow = True
		scoreLabel = myFont.render("You Reached Round: " + str(level), 1, green)
		quitLabel = myFont.render("QUIT", 1, white)
		while exitshow:
			gameDisplay.fill(black)
			gameDisplay.blit(exitLabel, (scrWidth*0.43, scrHeight*0.20))
			gameDisplay.blit(scoreLabel, (scrWidth*0.38, scrHeight*0.50))
			quitbutton = pygame.draw.rect(gameDisplay, red, [scrWidth*0.44, scrHeight*0.8, scrWidth*0.15, scrHeight*0.075])
			gameDisplay.blit(quitLabel, (scrWidth*0.485, scrHeight*0.823))
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
					exitshow = False
					startcontinue = False
					leadercontinue = False
					quitcontinue = False
					maincontinue = False
					gameContinue = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
					(pressed1,pressed2,pressed3) = pygame.mouse.get_pressed()
					#go back to home screen
					if quitbutton.collidepoint(pos) and pressed1 == 1:
						exitshow = False
						startcontinue = False
						leadercontinue = False
						quitcontinue = False
						maincontinue = False
						gameContinue = False


pygame.quit()
