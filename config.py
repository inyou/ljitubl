#!/usr/bin/python
# -*- coding: utf-8 -*-
# AIR Version : 1.0.0
import time
import pickle
import random
repertoire_origine="/home/pi/air/"

boxid=""
pks=""
temps_cycle=0
error=0
err_res=0
reboot=0
cycle=0
url=""
langue=""
verbosity_audio=0
version=0
ultra_port=''
port=0
volumeson=100



def load_objet(fic):
    objet={}
    try:
        with open(repertoire_origine+fic, 'rb') as fichier:
            mon_pickler = pickle.Unpickler(fichier)
            objet=mon_pickler.load()
    except:
        print "FICHIER "+repertoire_origine+fic+" innexistant"
    return objet

def dump_objet(fic,obj):
    with open(repertoire_origine+fic, 'wb') as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(obj)

def save_config():
    t=[boxid,pks,temps_cycle,error,err_res,reboot,cycle,url,langue,verbosity_audio,version,ultra_port,port]
    dump_objet("config.save",t)
    
    
def print_config():
    print boxid,pks,temps_cycle,error,err_res,reboot,cycle,url,langue,verbosity_audio,version,ultra_port,port
 
t=load_objet("config.save")
boxid,pks,temps_cycle,error,err_res,reboot,cycle,url,langue,verbosity_audio,version,ultra_port,port=t   
print_config()
#s="https://www.med-in-box.fr/agahtir/blink.php?id="+boxid+"&pks="+pks+"&date="+str(int(time.time()))+"&gly="+str(random.randint(0,100))
#dump_objet("atsend/"+str(int(time.time()))+".dat",s)