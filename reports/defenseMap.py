#!/usr/bin/env python2.7

# import modules
import pygame
import os

# initialize screen
pygame.init()
finished = False
showGrid = False
screenWidth = 800
screenHeigth = 600
pygame.display.set_caption("Tower Defense")
myFont = pygame.font.SysFont("monospace", 30)
label = myFont.render("Press 'g' to toggle grid on/off", 1, (0, 0, 0))
screen = pygame.display.set_mode((screenWidth, screenHeigth))
level1Map = pygame.image.load("Images/level1Map.png")
level1Map = pygame.transform.scale(level1Map, (screenWidth, screenHeigth))
level1MapRect = level1Map.get_rect()

# initialize field matrix
mapMatrix = [[0 for i in range(20)] for i in range(15)]
for row in range(15):
	for column in range(20): print "{}  ".format(mapMatrix[row][column]),
	print '\n'

# run game
while not finished:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
			finished = True
		if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
			showGrid = not showGrid

	screen.fill((0, 0, 0))
	screen.blit(level1Map, level1MapRect)
	if showGrid:
		for x in xrange(0, screenWidth, 40):
			pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, screenHeigth))
		for y in xrange(0, screenHeigth, 40):
			pygame.draw.line(screen, (0, 0, 0), (0, y), (screenWidth, y))
	screen.blit(label, (50, 490))
	pygame.display.flip()
