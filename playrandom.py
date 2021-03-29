#!/usr/bin/env python
import os, random, sys, select, time
import gpiozero
import datetime as dt
from datetime import datetime
import logging

# change this value based on which GPIO port the relay is connected to
RELAY_PIN = 18

# create a relay object. (https://gist.github.com/johnwargo/ea5edc8516b24e0658784ae116628277#file-relay-test-py)
# Triggered by the output pin going low: active_high=False.
# Initially off: initial_value=False
relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)

# Time range for lower frequency
nightBegin = '08:00PM'
nightEnd = "07:00AM"

def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime < endTime:
        return nowTime >= startTime and nowTime <= endTime
    else: #Over midnight
        return nowTime >= startTime or nowTime <= endTime

def set_relay(status):
    if status:
        print("Setting relay: ON")
        relay.on()
    else:
        print("Setting relay: OFF")
        relay.off()

def toggle_relay():
    print("toggling relay")
    relay.toggle()

def rndmp3 ():   

  while 1:
	#logging.basicConfig(filename='gull.log', level=logging.INFO)
	
	set_relay(True) #Turn on Amp
	
	time.sleep(5) #Wait till Amp has full power
	
    	randomfile = random.choice(os.listdir("./mp3")) #Pick a random gullfucker sound
	print "Playing file" ,randomfile,"..." 
    	file = ' ./mp3/'+ randomfile
    	os.system ('mpg123 ' + file)
	set_relay(False) #Turn Amp off
	
	now = datetime.now()
	timeEnd = datetime.strptime(nightEnd, "%I:%M%p")
	timeStart = datetime.strptime(nightBegin, "%I:%M%p")
	timeNow = now.strftime("%I:%M%p")
	timeNow = datetime.strptime(timeNow, "%I:%M%p")
 	
	print(isNowInTimePeriod(timeStart, timeEnd, timeNow))
 
	
	if  isNowInTimePeriod(timeStart, timeEnd, timeNow):
        	x = random.randint(3600,7200)
		print("Starting Nighttime Countdown!")
		while x>0:
			sys.stdout.write("\r" + str(x))
			sys.stdout.flush()
			time.sleep(1)
			x-=1
		print(" ")
		print("Playing!")
    	else:
		x = random.randint(1800,3600)
                print("Starting Daytime Countdown!")
                while x>0:
                        sys.stdout.write("\r" + str(x))
                        sys.stdout.flush()
                        time.sleep(1)
                        x-=1
		print(" ")
                print("Playing!")

	
set_relay(False)
time.sleep(1)
set_relay(True)
time.sleep(1)
set_relay(False)
rndmp3 ()
