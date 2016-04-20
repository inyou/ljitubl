#!/usr/bin/python
import config
import time

def save_data(tab):
    s=config.url+"?id="+config.boxid+"&pks="+config.pks+"&date="+str(tab[1])
    if tab[0]=="ten":
        s=s+"&sys="+str(tab[2])+"&dia="+str(tab[3])+"&pul="+str(tab[4])
        config.dump_objet("atsend/"+str(tab[1])+"."+tab[0],s)
    if tab[0]=="poi":
        s=s+"&poi="+str(tab[2])
        config.dump_objet("atsend/"+str(tab[1])+"."+tab[0],s)
    if tab[0]=="tem":
        s=s+"&tem="+str(tab[2])
        config.dump_objet("atsend/"+str(tab[1])+"."+tab[0],s)
    if tab[0]=="gli":
        s=s+"&gly="+str(tab[2])
        config.dump_objet("atsend/"+str(tab[1])+"."+tab[0],s)
    # if tab[0]=="oxy":
    # if tab[0]=="act":
    # if tab[0]=="ecg":
    # if tab[0]=="ala":
    # if tab[0]=="ult":
