#!/usr/bin/python

import subprocess
import config
import temp
import poids
import tens
import gluco
import speech
import sender
import time
import os

while (True):
    try:
        commande="sudo hcitool2 lescan;exit 0"
        device=subprocess.check_output(commande, shell=True)
        print device
        if (device.find("Set scan parameters failed: Input/output error")>=0):
            os.system("sudo hciconfig hci0 down; sudo hciconfig hci0 up;exit 0")
        else:
            device_name = [str(x) for x in device.split('#')]
            device_name=device_name[1:3]
            print device_name
            if device_name[1]=="FORA IR21":
                t=temp.temperature(device_name[0])
                sender.save_data(["tem",int(time.time()),t[0]])
                speech.temperature(t[0])
            if device_name[1]=="FORA IR21b":
                t=temp.temperature(device_name[0])
                sender.save_data(["tem",int(time.time()),t[0]])
                speech.temperature(t[0])
            if device_name[1]=="KNV V125":
                p=poids.poids(device_name[0])
                print p, type(p)
                if (p==None) or (p<=5.0):
                    speech.poidsbas()
                else:
                    sender.save_data(["poi",int(time.time()),p])
                    speech.poids(p)
            if device_name[1]=="Diamond Balance":
                p=poids.poids(device_name[0])
                print p, type(p)
                if (p==None) or (p<=5.0):
                    speech.poidsbas()
                else:
                    sender.save_data(["poi",int(time.time()),p])
                    speech.poids(p)
            if device_name[1]=="DIAMOND CUFF BP":
                te=tens.tension(device_name[0])
                sender.save_data(["ten",int(time.time()),te[0][0],te[0][1],te[0][2]])
                speech.tension(te[0][0],te[0][1],te[0][2])
            if device_name[1]=="DIAMOND MOBILE ":
                g=gluco.gluco(device_name[0])
                sender.save_data(["gli",int(time.time()),g[0]])
                speech.glicemie(g[0])
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to be printed directly
        pass