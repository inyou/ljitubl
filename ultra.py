#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : 5.0.0
"""
la class ultra est un Tread permettant de recuperer le poids de la balance Ultraship U-2 sur le port série.
"""
import time
import serial
import speech
from threading import Thread
import config

def connect():
    """
    Connecte le port série de la balance Ultraship U-2
    """
    try:
        ser=serial.Serial()
        ser.port=config.ultra_port
        ser.baudrate=9600
        ser.timeout=None
        ser.bytesize=8
        ser.parity='N'
        ser.sotpbits=1
        ser.open()
        return ser
    except:
        return None
def deconnect(ser):
    """
    Déconnecte le port série de la balance Ultraship U-2
    """
    ser.close()
def recoit(ser):
    """
    Recoit récupère les messages de la balance Ultraship U-2
    """
    t=""
    if (ser.inWaiting()>13):
            time.sleep(1)
            while ser.inWaiting()>0:
                    t=t+ser.read(ser.inWaiting())
    return t
def trans(t):
    """
    Trans décripte les messages recu de la balance Ultraship U-2
    """
    k=""
    p=""
    key=ord(t[1])^0x26
    for i in range(3,11):
            p=p+chr(ord(t[i])^key)
    print p+"kg"
    print
    return p[2:]
    
class ultra(Thread):
    def __init__(self):
        """
        Initialise la class ultra
        """
        Thread.__init__(self)
        self.running=False
        self.type=0
    def run(self):
        """
        Lance le thread et recupere le poids
        """
        self.running=True
        spt=[1,1,2,2,3,3,4,4]
        speech.pesezpoche(spt[self.type-1])
        if self.running==True:
            speech.manipbalance()
            s=connect()
            if s==None:
                speech.attentionbalancedeconnecte()
            else:  
                bouclepoids=True
                poids=0.0
                while bouclepoids:
                    if self.running==False:
                        bouclepoids=False
                    t=recoit(s)
                    if t<>"" and len(t)==14:
                        poids=trans(t)
                        try:
                            print float(poids)
                            bouclepoids=False
                        except:
                            t=""
                            speech.rappuyezsend()
                if self.running==True:        
                    deconnect(s)
                    #Zone d'envoye de fichier
                    print float(poids)
                    s="https://www.med-in-box.fr/agahtir/blink.php?id="+config.boxid+"&pks="+config.pks+"&date="+str(int(time.time()))+"&typ="+str(self.type)+"&poc="+str(float(poids))
                    print s
                if self.running==True:  
                    config.dump_objet("atsend/"+str(int(time.time()))+".poc",s)
                if self.running==True:  
                    speech.poidspoche(float(poids))
                    print float(poids)
            self.running=False
    def settype(self,i):
        """
        Configure le type de poche à récupérer
        """
        self.type=i
    def stop(self):
        """
        Stop le Thread ultra
        """
        self.running=False
    def isrunning(self):
        """
        Verifie si le thread est en train d'être exécuté.
        """
        return self.running

