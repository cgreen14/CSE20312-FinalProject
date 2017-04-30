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

# Start up window
#pygame.init()
#pygame.display.set_caption("Local Leaders")
#clock = pygame.time.Clock()
#gameDisplay = pygame.display.set_mode((scrWidth, scrHeight))
#pygame.quit();
#find if file exists, if not make one
if not os.path.isfile('./test.txt'): #create file
	file = open("test.txt", "w+")
	for i in range(5):
		file.write("empty" + str(i) + ",0\n")
	file.close()

file = open("test.txt", "r")

#Display Top 5 Names
scores = {}
for line in file:
	name = line.split(",")[0].rstrip()
	score = line.split(",")[1].rstrip()
	scores[name] = score

sortScore = sorted(scores, key=scores.get, reverse = True)

for s in sortScore:
	if scores[s] == "0":
		print "EMPTY", "0"
	else:
		print s, scores[s]
	
file.close()
