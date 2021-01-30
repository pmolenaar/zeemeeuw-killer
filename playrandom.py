#!/usr/bin/env python
import os, random, sys, select, time
import gpiozero

# change this value based on which GPIO port the relay is connected to
RELAY_PIN = 18

# create a relay object. (https://gist.github.com/johnwargo/ea5edc8516b24e0658784ae116628277#file-relay-test-py)
# Triggered by the output pin going low: active_high=False.
# Initially off: initial_value=False
relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)

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
	
    	randomfile = random.choice(os.listdir("/home/pi/mp3"))
	print "Playing file" ,randomfile,"..."
    	file = ' /home/pi/mp3/'+ randomfile
    	os.system ('omxplayer -o local' + file)
	
	set_relay(False) #Turn Amp off
	
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

set_relay(False)
time.sleep(1)
set_relay(True)
time.sleep(1)
set_relay(False)
rndmp3 ()

