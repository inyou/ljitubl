#!/usr/bin/python
# -*- coding: utf-8 -*-

import bluepy.btle
import time
import subprocess

class MyDelegate(bluepy.btle.DefaultDelegate):
    def __init__(self,hndl):
        bluepy.btle.DefaultDelegate.__init__(self)
        self.hndl=hndl;
        self.poids=None;
        # ... initialise here

    def handleNotification(self, cHandle, data):
        # ... perhaps check cHandle
        # ... process 'data'
        if (cHandle==self.hndl):
            if data[0]=="U":
                self.poids=(ord(data[1])*256+ord(data[2]))/10.0
    def get_poids(self):
        return self.poids
    
def poids(devAddr):
    try:
        addrType = "public"
        print("Connecting to: {}, address type: {}".format(devAddr, addrType))
        conn = bluepy.btle.Peripheral(devAddr, addrType)
        try:
            #conn.getServices()
            print "Connecté"
            my=MyDelegate(0x52)
            conn.setDelegate(my)
            conn.writeCharacteristic(0x53,chr(3)+chr(3), withResponse=True)
            trouve=True    
            while trouve:
                if conn.waitForIndicates(1.):
                    trouve=False
                    #conn.disconnect()
        finally:
            print "Poids : ",my.get_poids()           
            print "Déconnection"
    except bluepy.btle.BTLEException as e:
        #print "Exception bluetooth",e
        pass
    return my.get_poids()

