#!/usr/bin/python
# -*- coding: utf-8 -*-
# AIR Version : 1.0.0
import config
import time
import subprocess
import serial
import urllib2
import shutil
import os
from os import listdir
from os.path import isfile, join
import ssl


def test_cyclique():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        s="http://www.med-in-box.fr/agahtir/blink.php"+"?id="+config.boxid+"&pks="+config.pks+"&date="+str(int(time.time()))+"&err="+str(config.error)+"&res="+str(config.err_res)+"&reb="+str(config.reboot)+"&cyc="+str(config.cycle)
        h=urllib2.urlopen(s,timeout=5,context=ctx) 
    except:
        #erreur de réseau.
        config.err_res=config.err_res+1
        print "erreur reseau 1"
        return False
    if h.getcode()==200:
        cmd=h.read()
        if cmd!="":
            os.system(cmd)
    else:
        config.err_res=config.err_res+1
        print "erreur reseau 2"
        return False
    return True


def envoie_data():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    #Cherche les fichiers dans atsend et les place dans le tableau onlyfiles
    onlyfiles = [ f for f in listdir(config.repertoire_origine+"atsend/") if isfile(join(config.repertoire_origine+"/atsend/",f))]
    # Trie onlyfiles par ordre croissant
    onlyfiles.sort()
    for i in onlyfiles:
        print onlyfiles
        a=config.load_objet("atsend/"+i)
        ok=True
        print a
        if (len(a)>42)and(a[0:42]!="https://www.med-in-box.fr/agahtir/blink.php"):
            shutil.move(config.repertoire_origine+"atsend/"+i,config.repertoire_origine+"err/"+i)
            time.sleep(1)
        else:
            try:
                h=urllib2.urlopen(a,timeout=5,context=ctx)
            except:     
                ok=False
                config.err_res=config.err_res+1
                print "erreur reseau 3"
                time.sleep(3)
            if ((ok)and(h.getcode()==200)):
                shutil.move(config.repertoire_origine+"atsend/"+i,config.repertoire_origine+"sent/"+i)
                time.sleep(1)

def service():
    statutcon=False;
    config.reboot=config.reboot+1
    config.err_res=0
    config.error=0
    config.cycle=0
    t=time.time()
    test_cyclique()
    while True:
        if (config.cycle<5):
            if (t+20<time.time()): # toutes les temps_cycle secondes envoie trame de suivie et si heure mal régler regle l'heure
                t=time.time()
                statutcon=test_cyclique()
                config.cycle=config.cycle+1
        if (t+config.temps_cycle<time.time()): # toutes les temps_cycle secondes envoie trame de suivie et si heure mal régler regle l'heure
            t=time.time()
            statutcon=test_cyclique()
            config.cycle=config.cycle+1
        # PARCOUR LES FICHIER DANS atsend les envoies et si il reussit il les places dans sent
        if statutcon==True:
            envoie_data()
            time.sleep(1)
        
service()
