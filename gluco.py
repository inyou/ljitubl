#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluepy.btle
import speech
class MyDelegate(bluepy.btle.DefaultDelegate):
    def __init__(self,hndl):
        bluepy.btle.DefaultDelegate.__init__(self)
        self.hndl=hndl
        self.gluco=None
        # ... initialise here

    def get_gluco(self):
        return self.gluco
    def handleNotification(self, cHandle, data):
        # ... perhaps check cHandle
        # ... process 'data'
        if (cHandle==self.hndl):
            #print ">>>",data
            #for i in data:
            #    print hex(ord(i)),
            if (ord(data[1])==0x26):
                self.gluco=ord(data[2])
    
def function_calctemp(a,b,c,d):
    tempdata=long(a+256*(b+256*(c+256*d)))
    mantissa=long(tempdata & 0x00FFFFFF)
    temp=mantissa/100.0
    return temp

def gluco(devAddr):
    try:
        addrType = "random"
        print("Connecting to: {}, address type: {}".format(devAddr, addrType))
        conn = bluepy.btle.Peripheral(devAddr, addrType)
        bat=conn.readCharacteristic(0x17)
        try:
            my=MyDelegate(0x20)
            conn.setDelegate(my)
            conn.writeCharacteristic(0x21,chr(1)+chr(1), withResponse=True)
            conn.writeCharacteristic(0x20,chr(0x51)+chr(0x26)+chr(0x0)+chr(0x0)+chr(0x0)+chr(0x0)+chr(0xa3)+chr(0x1A), withResponse=True)
            trouve=True    
            while trouve:
                if conn.waitForNotifications(1.):
                    trouve=False
        finally:
            print "Glicémie : ",my.get_gluco()," battery : ",ord(bat)
            conn.writeCharacteristic(0x20,chr(0x51)+chr(0x52)+chr(0x0)+chr(0x0)+chr(0x0)+chr(0x0)+chr(0xa3)+chr(0x46), withResponse=True)
            mesdeb=str(chr(0x51)+chr(0x50)+chr(0x0)+chr(0x0)+chr(0x0)+chr(0x0)+chr(0xa3)+chr(0x44))
            conn.writeCharacteristic(0x20,mesdeb, withResponse=True)
            conn.disconnect()
        return my.get_gluco(),ord(bat)
    except (bluepy.btle.BTLEException):
        speech.lostgluco()
        print "Exception bluetooth"
        conn.disconnect()
        print "Déconnection"