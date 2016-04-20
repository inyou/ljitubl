#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluepy.btle
import time
import subprocess
import speech

class MyDelegate(bluepy.btle.DefaultDelegate):
    def __init__(self,hndl):
        bluepy.btle.DefaultDelegate.__init__(self)
        self.hndl=hndl;
        self.tens=None
        # ... initialise here

    def handleNotification(self, cHandle, data):
        # ... perhaps check cHandle
        # ... process 'data'
        if (cHandle==self.hndl):
            self.tens=ord(data[1]),ord(data[3]),ord(data[14])
    def get_tens(self):
        return self.tens
class MyDelegate2(bluepy.btle.DefaultDelegate):
    def __init__(self,hndl):
        bluepy.btle.DefaultDelegate.__init__(self)
        self.hndl=hndl;
        self.mes54=False;
        # ... initialise here

    def handleNotification(self, cHandle, data):
        # ... perhaps check cHandle
        # ... process 'data'
        if (cHandle==self.hndl):
            if (data==str(chr(0x51)+chr(0x54)+chr(0x0)+chr(0x0)+chr(0x0)+chr(0x0)+chr(0xa5)+chr(0x4a))):
                self.mes54=True
    def getmes54(self):
        return self.mes54

def tension(devAddr):
    m1=None
    bat=None
    try:
        addrType = "random"
        print("Connecting to: {}, address type: {}".format(devAddr, addrType))
        conn = bluepy.btle.Peripheral(devAddr, addrType)
        print "Connecté"
        time.sleep(5)
        print "Commande prend la tension!!!"
        bat=conn.readCharacteristic(0x14)
        mesdeb=str(chr(0x51)+chr(0x43)+chr(0x0)+chr(0x0)+chr(0x6)+chr(0x0)+chr(0xa3)+chr(0x3d))
        conn.writeCharacteristic(0x1d,mesdeb, withResponse=True)
        try:
            m2=MyDelegate2(0x1d)
            conn.setDelegate(m2)
            conn.writeCharacteristic(0x1e,chr(3)+chr(3), withResponse=True)
            trouve=True    
            while trouve:
                if m2.getmes54():
                        conn.writeCharacteristic(0x0f,chr(3)+chr(3), withResponse=True)
                        m1=MyDelegate(0x0e)
                        conn.setDelegate(m1)
                        trouve=False
                if conn.waitForNotifications(1.):
                    pass
                if conn.waitForIndicates(1.):
                    trouve=False
                    pass
        finally:
            conn.writeCharacteristic(0x1d,chr(0x51)+chr(0x52)+chr(0x0)+chr(0x0)+chr(0x0)+chr(0x0)+chr(0xa3)+chr(0x46), withResponse=True)
            mesdeb=str(chr(0x51)+chr(0x50)+chr(0x0)+chr(0x0)+chr(0x0)+chr(0x0)+chr(0xa3)+chr(0x44))
            conn.writeCharacteristic(0x1d,mesdeb, withResponse=True)
            conn.disconnect()
            print "Tension:",m1.get_tens(),"baterry:",ord(bat)
            print "Déconnection"
    except (bluepy.btle.BTLEException):
        speech.losttensiometre()
        print "Exception bluetooth"
        conn.disconnect()
        print "Déconnection"
    return m1.get_tens(),ord(bat)