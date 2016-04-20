#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluepy.btle
import speech
class MyDelegate(bluepy.btle.DefaultDelegate):
    def __init__(self,hndl):
        bluepy.btle.DefaultDelegate.__init__(self)
        self.hndl=hndl
        self.temp=None
        # ... initialise here
    def set_temp(self,val):
        self.temp=val
    def get_temp(self):
        return self.temp
    def handleNotification(self, cHandle, data):
        # ... perhaps check cHandle
        # ... process 'data'
        if (cHandle==self.hndl): 
            #print "Température",function_calctemp(ord(data[1]),ord(data[2]),ord(data[3]),ord(data[4]))
            self.set_temp(function_calctemp(ord(data[1]),ord(data[2]),ord(data[3]),ord(data[4])))
    
def function_calctemp(a,b,c,d):
    tempdata=long(a+256*(b+256*(c+256*d)))
    mantissa=long(tempdata & 0x00FFFFFF)
    temp=mantissa/100.0
    return temp

def temperature(devAddr):
    try:
        addrType = "random"
        print("Connecting to: {}, address type: {}".format(devAddr, addrType))
        conn = bluepy.btle.Peripheral(devAddr, addrType)
        bat=conn.readCharacteristic(0x12)
        
        #print "Battery : >",bat,"<",ord(bat)
        try:
            my=MyDelegate(0x0e)
            conn.setDelegate(my)
            conn.writeCharacteristic(0x0f,chr(3)+chr(3), withResponse=True)
            trouve=True    
            while trouve:
                if conn.waitForIndicates(1.):
                    trouve=False
        finally:
            print "Temperature : ",my.get_temp()," battery : ",ord(bat)
            mesdeb=str(chr(0x51)+chr(0x50)+chr(0x0)+chr(0x0)+chr(0x0)+chr(0x0)+chr(0xa3)+chr(0x44))
            conn.writeCharacteristic(0x1b,mesdeb, withResponse=True)
            conn.disconnect()
        return my.get_temp(),ord(bat)
    except (bluepy.btle.BTLEException):
        speech.lostthermometre()
        print "Exception bluetooth"
        conn.disconnect()
        print "Déconnection"
