#test script to practice scripting eqmod mount

#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# You must initialize the gobject/dbus support for threading
# before doing anything.
 
import gobject
import os
import time
import signal

#timeout
def handler(signum, frame):
    print "Process has timed out"
    raise Exception("devices not found")
    
gobject.threads_init()
 
from dbus import glib
glib.init_threads()
 
# Create a session bus.
import dbus
bus = dbus.SessionBus()
 
# Create an object that will proxy for a particular remote object.
remote_object = bus.get_object("org.kde.kstars", # Connection name
                               "/KStars/INDI" # Object's path
                              )
 
#Introspection returns an XML document containing information
#about the methods supported by an interface.
print ("Introspection data:\n")
print remote_object.Introspect()

# Get INDI interface
iface = dbus.Interface(remote_object, 'org.kde.kstars.INDI')

myDevices = [ "indi_eqmod_telescope"]

#start INDI devices
iface.start("7624", myDevices)
print ("Introspection data:\n")
print iface.Introspect()
print ("Waiting for INDI devices...")

#Create array for recieved devices

    
signal.signal(signal.SIGALRM, handler)
signal.alarm(20)
#devices

devices = []

def cArrayDevices():
    while True:
        devices = iface.getDevices()
        if (len(devices) < len(myDevices)):
            time.sleep(1)
        else:
            break;

try:
    cArrayDevices()
except Exception, exc:
    print exc
    
signal.alarm(0)
        
print ("We received the following devices:")
for device in devices:
    print device

# Set connect switch to ON to connect the devices
iface.setSwitch("EQMod Mount", "CONNECTION", "CONNECT", "On")
# Send the switch to INDI server so that it gets processed by the driver
iface.sendProperty("EQMod Mount", "CONNECTION")

telescopeState = "Busy"

# Wait until devices are connected
while True:
    telescopeState = iface.getPropertyState("EQMod Mount", "CONNECTION")
    if (telescopeState != "Ok"):
        time.sleep(1)
    else:
        break

print "Connected to Telescope and CCD is established."


time.sleep(30)


# Stop INDI server
print ("Shutting down INDI server...")
iface.stop("7624")



