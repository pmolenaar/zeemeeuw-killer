#!/usr/bin/env python
import os, random, sys, select


def rndmp3 ():   

  while 1:
	
    	randomfile = random.choice(os.listdir("/home/pi/mp3"))
	print "Playing file" ,randomfile,"..."
    	file = ' /home/pi/mp3/'+ randomfile
    	os.system ('omxplayer -o local' + file)
	
	pause = random.randint(min,max)
	
	print "Hit Key and press Enter to stop. Waiting for", pause, "seconds"
	i, o, u = select.select( [sys.stdin], [], [], pause )
	if (i):
		print "STOPPED", sys.stdin.readline().strip()
		break
	else:
		print "next"

os.system("clear") # Clear Screen

# defining waiting time range
min = 0
max = 35

print "Audio Random Player Runnning. Waiting Time from ",min,"to",max, "seconds."

rndmp3 ()

