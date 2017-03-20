#!/usr/bin/env python2.7

import pygame
import math
import sys
import os

try:
	import pygame
except:
	os.system('pip install pygame')
    	import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
pi = math.pi
theta = dtheta = 0
clock = pygame.time.Clock()

def drawBackground():
    pygame.draw.rect(screen,(0,128,255),pygame.Rect(300,250,40,40))
    pygame.draw.rect(screen,(0,128,0),pygame.Rect(300,210,40,40))
    pygame.draw.rect(screen,(0,128,255),pygame.Rect(300,170,40,40))
    pygame.draw.polygon(screen,(0,128,0),[[300,170],[340,170],[320,140]])

def rotateLines(xCenter, yCenter, theta, radius):
  x1 = xCenter - math.cos(theta)*radius;
  x2 = xCenter + math.cos(theta)*radius;
  y1 = yCenter - math.sin(theta)*radius;
  y2 = yCenter + math.sin(theta)*radius;

  x3 = xCenter - math.cos(theta+pi/2)*radius;
  x4 = xCenter + math.cos(theta+pi/2)*radius;
  y3 = yCenter - math.sin(theta+pi/2)*radius;
  y4 = yCenter + math.sin(theta+pi/2)*radius;

  pygame.draw.aaline(screen,(255,255,255),[x1,y1],[x2,y2],True)
  pygame.draw.aaline(screen,(255,255,255),[x3,y3],[x4,y4],True)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dtheta -= 1
            elif event.key == pygame.K_RIGHT:
                dtheta += 1

    screen.fill((0,0,0))
    drawBackground()
    rotateLines(320, 140, theta, 30)

    theta = theta +(0.1*dtheta)
    pygame.display.flip()
    clock.tick(60)
