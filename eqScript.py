

# Initialising gobject/dbus support for threading
import gobject
import os
import time

gobject.threads_init()

from dbus import glib
glib.init_threads()

#Creating session bus.
import dbus
bus = dbus.SessionBus()

#Creating proxy object for remote object
remote_object = bus.get_object("org.kde.kstars",
                               "/KStars/INDI"
                               )

#Get XML document of methods supported by interface
print ("Introspection data:\n")
print remote_object.Introspect()

#INDI interface
iface = dbus.Interface(remote_object, 'org.kde.kstars.INDI')

myDevices = [ "indi_simulator_telescope", "indi_simulator_ccd" ]

#Initialising array of detected INDI devices
iface.start("7634", myDevices)
print "Waiting for INDI devices..."
devices = []

while True:
    devices = iface.getDevices()
    if (len(devices) < len(myDevices)):
        time.sleep(1)
    else:
        break;

print "The following devices were detected:"
for device in devices
    print device

print "Establishing connection to Telescope and CCD..."

#Set connect switch to ON to connect the devices
iface.setSwitch("Telescope simulator", "CONNECTION", "CONNECT", "On")
#Send the switch to INDI server so that it gets processed by the driver
iface.sendProperty("Telescope Simulator", "CONNECTION")
#Same thing for CCD simulator
iface.setSwitch("CCD Simulator", "CONNECTION", "CONNECT", "On")
iface.sendProperty("CCD Simulator", "CONNECTION")

TELESCOPEsTATE      = "Busy"
ccdState            = "Busy"

#Wait until devices are connected
while True:
    telescopeState = iface.getPropertyState("Telescope Simulator", "CONNECTION")













#ERROR HANDLING

##timeout process function
#def timeoutP():
#    while 1:
#        print "sec"
#        time.sleep(1)
#
#signal.signal(signal.SIGALRM, handler)
#signal.alarm(10)
#try:
#    timeoutP()
#except Exception, exc:
#    print exc
#signal.alarm(0)



