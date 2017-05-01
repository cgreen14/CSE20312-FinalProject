#!/usr/bin/env python2.7

import sys
import os
import time
import math
import pygame

# Initialize Variables #
scrWidth = 800
scrHeight = 600
FPS = 30
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
filen = 'board.txt'
ycords = [0.3, 0.4, 0.5, 0.6, 0.7]

# Start up window
pygame.init()
pygame.display.set_caption("Local Leaders")
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((scrWidth, scrHeight))
myfont = pygame.font.SysFont("Britannic Bold", 30)
namefont = pygame.font.SysFont("Britannic Bold", 25)
#Titles
nameLabel = myfont.render("NAME", 1, red)
scoreLabel = myfont.render("SCORE", 1, red)
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
	score = line.split(",")[1].rstrip()
	scores[name] = score
sortScore = sorted(scores, key=lambda x: int(scores[x]), reverse = True)
for s in sortScore:
	if scores[s] == "0":
		print "EMPTY", "0"
	else:
		print s, scores[s]

leader = True
while leader:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
			leader = False
	gameDisplay.fill((0,0,0))
	gameDisplay.blit(nameLabel, (scrWidth*0.30, scrHeight*0.20))
	gameDisplay.blit(scoreLabel, (scrWidth*0.55, scrHeight*0.20))
	for i,s in enumerate(sortScore):
		if scores[s] == "0":
			userLabel = namefont.render("XXX", 1, red)
			ypos = scrHeight*ycords[i]
			gameDisplay.blit(userLabel, (scrWidth*0.31, ypos))
		else:
			userLabel = namefont.render(s, 1, red)
			ypos = scrHeight*ycords[i]
			gameDisplay.blit(userLabel, (scrWidth*0.31, ypos))


	pygame.display.flip()


pygame.quit()
file.close()
