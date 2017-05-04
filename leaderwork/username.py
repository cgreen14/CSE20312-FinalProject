#!/usr/bin/env python2.7
import sys
import os
import time
import math
import pygame

filen = 'board.txt'

if not os.path.isfile(filen): #create file
	file = open(filen, "w+")
	for i in range(5):
		file.write("empty" + str(i) + ",0\n")
	file.close()
username = "XXX"
prevUser = set()
#read in username
print "\nPlease Insert You Username (3 characters)\n" 
works = False
while not works:
	name = raw_input()
	username = str(name)
	if len(name) == 3:
		works = True
	else:
		print "Please Insert Valid Name"


