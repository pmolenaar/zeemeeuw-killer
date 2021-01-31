#!/usr/bin/env python
import os, random, sys, select, time
import gpiozero
import datetime as dt

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
	set_relay(True) #Turn on Amp
	
	time.sleep(5) #Wait till Amp has full power
	
    	#randomfile = random.choice(os.listdir("/home/pi/mp3")) #Pick a random gullfucker sound
	randomfile = random.choice(os.listdir("~/mp3")) #Pick a random gullfucker sound
	print "Playing file" ,randomfile,"..." 
    	file = ' /home/pi/mp3/'+ randomfile
#    	os.system ('omxplayer -o local' + file)
	os.system ('afplay ' + file)	
	set_relay(False) #Turn Amp off
	
	timeEnd = datetime.strptime(nightEnd, "%I:%M%p")
	timeStart = datetime.strptime(nightEegin, "%I:%M%p")
	now = datetime.now()
    	currentTime = now.strftime("%I:%M%p")
	
	print(isNowInTimePeriod(timeStart, timeEnd, currentTime))
 
	
	if  print(isNowInTimePeriod(timeStart, timeEnd, currentTime)):
        	print('Night')
        	print(current_time)
        	pause = random.randint(min_slow,max_slow)
    	else:
        	print('Day')
        	print(current_time)
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
min_fast = 1800
max_fast = 3600
min_slow = 3600
max_slow = 7200

print "Audio Random Player Runnning. Waiting Time from ",min,"to",max, "seconds."

set_relay(False)
time.sleep(1)
set_relay(True)
time.sleep(1)
set_relay(False)
rndmp3 ()
