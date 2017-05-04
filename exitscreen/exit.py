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
yellow = (200, 200, 0)
orange = (255, 165 ,0 )
colorlist = [green, blue, white, yellow, orange]
filen = 'board.txt'
ycords = [0.3, 0.4, 0.5, 0.6, 0.7]

username = "RJG"
gameScore = 5

#start screen
pygame.init()
pygame.display.set_caption("End")
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((scrWidth, scrHeight))
myfont = pygame.font.SysFont("Britannic Bold", 30)
namefont = pygame.font.SysFont("Britannic Bold", 25)
#display score
exitLabel = myfont.render("GAME OVER", 1, white)
scoreLabel = myfont.render("You Reached Round: " + str(gameScore), 1, green)
#Update Leaderboard
if not os.path.isfile(filen): #create file
	file = open(filen, "w+")
	for i in range(5):
		file.write("empty" + str(i) + ",0\n")
	file.close()

file = open(filen, "a")
file.write(str(username)+","+str(gameScore)+"\n")
file.close()
exitshow = True
while exitshow:
    gameDisplay.fill(black)
    gameDisplay.blit(exitLabel, (scrWidth*0.43, scrHeight*0.20))
    gameDisplay.blit(scoreLabel, (scrWidth*0.38, scrHeight*0.50))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            exitshow = False

pygame.quit()
