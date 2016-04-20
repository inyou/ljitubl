#! /usr/bin/python
# -*- coding: utf-8 -*-
# Version : 5.0.0
import os
import random
import subprocess
import config
chem=config.repertoire_origine+"mp3"+"/"+config.langue[0:2]
def tension(sys,dia,pul):
    os.system("mpg123 -q "+chem+"/votretensionestde.mp3")
    os.system("mpg123 -q "+chem+"/systolic.mp3")
    os.system("mpg123 -q "+chem+"/"+str(sys)+".mp3")
    os.system("mpg123 -q "+chem+"/milimetredemercure.mp3")
    os.system("mpg123 -q "+chem+"/diastolic.mp3")
    os.system("mpg123 -q "+chem+"/"+str(dia)+".mp3")
    os.system("mpg123 -q "+chem+"/milimetredemercure.mp3")
    os.system("mpg123 -q "+chem+"/pulsation.mp3")
    os.system("mpg123 -q "+chem+"/"+str(pul)+".mp3")
    os.system("mpg123 -q "+chem+"/pulsationparminute.mp3")
def poids(poids):
    os.system("mpg123 -q "+chem+"/votrepoidsestde.mp3")
    virgule(poids)
    os.system("mpg123 -q "+chem+"/kilogrammes.mp3")
def glicemie(gli):
    os.system("mpg123 -q "+chem+"/votreglicemieestde.mp3")
    os.system("mpg123 -q "+chem+"/"+str(gli)+".mp3")
    os.system("mpg123 -q "+chem+"/mgdl.mp3")
def temperature(gli):
    os.system("mpg123 -q "+chem+"/votretemperatureestde.mp3")
    virgule(gli)
    os.system("mpg123 -q "+chem+"/degrescelcius.mp3")
def virgule(f):
    ent=int(f)
    v=int(f*10.0)-(ent*10)
    os.system("mpg123 -q "+chem+"/"+str(ent)+".mp3")
    os.system("mpg123 -q "+chem+"/virgule.mp3")
    os.system("mpg123 -q "+chem+"/"+str(v)+".mp3")
def virgule2(f):
    ent=int(f)
    v=int(f*10.0)-(ent*10)
    v2=int(f*100.0)-(ent*100)-(v*10)
    v3=int(f*1000.0)-(ent*1000)-(v*100)-(v2*10)
    os.system("mpg123 -q "+chem+"/"+str(ent)+".mp3")
    os.system("mpg123 -q "+chem+"/virgule.mp3")
    if (v*100+v2*10+v3)<257:
        os.system("mpg123 -q "+chem+"/"+str(v*100+v2*10+v3)+".mp3")
    else:
        os.system("mpg123 -q "+chem+"/"+str(v)+"00.mp3")
        os.system("mpg123 -q "+chem+"/"+str(v2)+str(v3)+".mp3")
def bonjour():
    os.system("mpg123 -q "+chem+"/bonjour.mp3")
def compte():
    for i in range(0,2):
        os.system("mpg123 -q "+chem+"/"+str(i)+".mp3")
def annulation():
    os.system("mpg123 -q "+chem+"/annulation.mp3")
def prenez_themperature():
    os.system("mpg123 -q "+chem+"/maintenanttemperature.mp3")
def prenez_glicemie():
    os.system("mpg123 -q "+chem+"/maintenantglicemie.mp3")
def prenez_tension():
    os.system("mpg123 -q "+chem+"/maintenanttension.mp3")
def prenez_poids():
    os.system("mpg123 -q "+chem+"/maintenantpoids.mp3")
def dit_tension():
    os.system("mpg123 -q "+chem+"/tension.mp3")
def dit_themperature():
    os.system("mpg123 -q "+chem+"/themperature.mp3")
def dit_poids():
    os.system("mpg123 -q "+chem+"/poids.mp3")
def protocolehd():
    if config.verbosity_audio==3:
        os.system("mpg123 -q "+chem+"/protocolehd.mp3")
    else:
        os.system("mpg123 --frames 110 "+chem+"/protocolehd.mp3")
def protocole2hd():
    if config.verbosity_audio==3:
        os.system("mpg123 -q "+chem+"/protocole2hd.mp3")
    else:
        os.system("mpg123 --frames 150 "+chem+"/protocole2hd.mp3")
def nouvelleserie():
    os.system("mpg123 -q "+chem+"/nouvelleserie.mp3")
def finhd():
    os.system("mpg123 -q "+chem+"/finhd.mp3")
def protocoledpca():
    if config.verbosity_audio==3:
        os.system("mpg123 -q "+chem+"/protocoledpca.mp3")
    else:
        os.system("mpg123 --frames 180 "+chem+"/protocoledpca.mp3")
def pesezpoche(i):
    if config.verbosity_audio==3:
        os.system("mpg123 -q "+chem+"/maintenantpoche.mp3")
        os.system("mpg123 -q "+chem+"/"+str(i)+".mp3")
    else:
        os.system("mpg123 -q "+chem+"/maintenantpoche.mp3")
        os.system("mpg123 -q "+chem+"/"+str(i)+".mp3")
def poidspoche(poids):
    if config.verbosity_audio==3:
        os.system("mpg123 -q "+chem+"/poidspoche.mp3")
        virgule2(poids)
        os.system("mpg123 -q "+chem+"/kilogrammes.mp3")
    else:
        virgule2(poids)
        os.system("mpg123 -q "+chem+"/kilogrammes.mp3")
def redemarrage():
    os.system("mpg123 -q "+chem+"/redemarrage.mp3")
    os.system("mpg123 -q "+chem+"/5.mp3")
    os.system("mpg123 -q "+chem+"/4.mp3")
    os.system("mpg123 -q "+chem+"/3.mp3")
    os.system("mpg123 -q "+chem+"/2.mp3")
    os.system("mpg123 -q "+chem+"/1.mp3")
    os.system("mpg123 -q "+chem+"/0.mp3")
def renvoie():
    os.system("mpg123 -q "+chem+"/renvoie.mp3")
def version():
    os.system("mpg123 -q "+chem+"/"+str(config.version)+".mp3")
def medecin():
    os.system("mpg123 -q "+chem+"/medecin.mp3")
def servicetechnique():
    os.system("mpg123 -q "+chem+"/servietechnique.mp3")
def langue():
    os.system("mpg123 -q "+chem+"/"+config.langue+".mp3")
def erreur():
    os.system("mpg123 -q "+chem+"/attentionerreur.mp3")
def erreur_num(a):
    os.system("mpg123 -q "+chem+"/attentionerreur.mp3")
    os.system("mpg123 -q "+chem+"/"+a+".mp3")
def douchecon():
    os.system("mpg123 -q "+chem+"/douchetteconnecte.mp3")
def douchedecon():
    os.system("mpg123 -q "+chem+"/douchettedeconnecte.mp3")
def sonplus():
    os.system("mpg123 -q "+chem+"/sonplus.mp3")
def sonmoins():
    os.system("mpg123 -q "+chem+"/sonmoins.mp3")
def configuration():
    os.system("mpg123 -q "+chem+"/configuration.mp3")
def manipthermometre():
    os.system("mpg123 -q "+chem+"/manipthermometre.mp3")
def manippesepersonne():
    os.system("mpg123 -q "+chem+"/manippesepersonne.mp3")
def maniptensiometre():
    os.system("mpg123 -q "+chem+"/maniptensiometre.mp3")
def manipbalance():
    if config.verbosity_audio==3:
        os.system("mpg123 -q "+chem+"/manipbalance.mp3")
def thermometreconfigurer():
    os.system("mpg123 -q "+chem+"/thermometreconfigurer.mp3")
def tensiometreconfigurer():
    os.system("mpg123 -q "+chem+"/tensiometreconfigurer.mp3")
def pesepersonneconfigurer():
    os.system("mpg123 -q "+chem+"/pesepersonneconfigurer.mp3")
def finconfiguration():
    os.system("mpg123 -q "+chem+"/finconfiguration.mp3")
def ecg():
    os.system("mpg123 -q "+chem+"/ecg.mp3")
def donnerecu():
    os.system("mpg123 -q "+chem+"/donnerecu.mp3")
def info_id():
    for i in config.boxid:
        os.system("mpg123 -q "+chem+"/"+i+".mp3")

def ok_son():
    os.system("mpg123 -q "+chem+"/stop.mp3")
def info_ip():
    a=subprocess.check_output("ifconfig; exit 0",stderr=subprocess.STDOUT,shell=True)
    try:
        a=a[a.index("eth0"):a.index("lo")]
        a=a[a.index("inet adr:"):a.index("Bcast")]
        a=a[a.index(":")+1:]
        b=a[:a.index(".")]
        t=a[a.index(".")+1:]
        c=t[:t.index(".")]
        t=t[t.index(".")+1:]
        d=t[:t.index(".")]
        t=t[t.index(".")+1:]
        e=t[:t.index(chr(32))]
    except:
        os.system("mpg123 -q "+chem+"/attentionerreur.mp3")
    if len(b)<=0 or len(b)>3:
        os.system("mpg123 -q "+chem+"/attentionerreur.mp3")
    else:
        os.system("mpg123 -q "+chem+"/"+b+".mp3")
        os.system("mpg123 -q "+chem+"/point.mp3")
        os.system("mpg123 -q "+chem+"/"+c+".mp3")
        os.system("mpg123 -q "+chem+"/point.mp3")
        os.system("mpg123 -q "+chem+"/"+d+".mp3")
        os.system("mpg123 -q "+chem+"/point.mp3")
        os.system("mpg123 -q "+chem+"/"+e+".mp3")
                                                                    #message alarme et ultrafiltration
def say_int(a): #dit un entier entre 0 et 256000
    if (a>=0) and (a<=200):
        os.system("mpg123 -q "+chem+"/"+str(a)+".mp3")
    elif (a>200) and (a<1000):
        b=int(a/100)*100
        os.system("mpg123 -q "+chem+"/"+str(b)+".mp3")
        if (a-b)>0:
            say_int(a-b)
    elif (a>=1000) and (a<1000000):
        b=int(a/1000)
        if b>1:
            say_int(b)
        os.system("mpg123 -q "+chem+"/1000.mp3")
        if (a-b*1000)>0:
            say_int(a-b*1000)
def say_intneg(a): #dit un entier entre 0 et 256000
    if (a<0):
        os.system("mpg123 -q "+chem+"/moins.mp3")
        say_int(-1*a);
    if (a>=0) and (a<=200):
        os.system("mpg123 -q "+chem+"/"+str(a)+".mp3")
    elif (a>200) and (a<1000):
        b=int(a/100)*100
        os.system("mpg123 -q "+chem+"/"+str(b)+".mp3")
        if (a-b)>0:
            say_int(a-b)
    elif (a>=1000) and (a<1000000):
        b=int(a/1000)
        if b>1:
            say_int(b)
        os.system("mpg123 -q "+chem+"/1000.mp3")
        if (a-b*1000)>0:
            say_int(a-b*1000)
def moins():
        os.system("mpg123 -q "+chem+"/moins.mp3")
  
def entrezalarme():
    os.system("mpg123 -q "+chem+"/entrezalarme.mp3")
def nbalarme(a):
    os.system("mpg123 -q "+chem+"/nbalarme.mp3")
    say_int(int(a))
def valider():
    os.system("mpg123 -q "+chem+"/valider.mp3")
def entrezultrafiltration():
    os.system("mpg123 -q "+chem+"/entrezultrafiltration.mp3")
def nbultrafiltration(a):
    os.system("mpg123 -q "+chem+"/ultrafiltration.mp3")
    say_int(int(a))
def changementpile():
    os.system("mpg123 -q "+chem+"/changementpile.mp3")
def losttensiometre():
    os.system("mpg123 -q "+chem+"/losttensiometre.mp3")
def lostbalance():
    os.system("mpg123 -q "+chem+"/lostbalance.mp3")
def lostthermometre():
    os.system("mpg123 -q "+chem+"/lostthermometre.mp3")
def lostgluco():
    os.system("mpg123 -q "+chem+"/lostgluco.mp3")
def poidbas():
    os.system("mpg123 -q "+chem+"/poidbas.mp3")
                                                                #message erreur balance précision
def attentionbalancedeconnecte():
    os.system("mpg123 -q "+chem+"/attentionbalancedeconnecte.mp3")
def rappuyezsend():
    os.system("mpg123 -q "+chem+"/rappuyezsend.mp3")
                                                                #message d'Aide
def presentation():
    os.system("mpg123 -q "+chem+"/presentation.mp3")
def installation():
    os.system("mpg123 -q "+chem+"/installation.mp3")
def aidebalance():
    os.system("mpg123 -q "+chem+"/aidebalance.mp3")
def aidepoche():
    os.system("mpg123 -q "+chem+"/aidepoche.mp3")
def aidetensiometre():
    os.system("mpg123 -q "+chem+"/aidetensiometre.mp3")
def aidethemperature():
    os.system("mpg123 -q "+chem+"/aidethemperature.mp3")
def problemetechnique():
    os.system("mpg123 -q "+chem+"/problemetechnique.mp3")
def problememedical():
    os.system("mpg123 -q "+chem+"/problememedical.mp3")
                                                                #Message test wifi
def connectionactive():
    os.system("mpg123 -q "+chem+"/connectionactive.mp3")
def aucuneconnection():
    os.system("mpg123 -q "+chem+"/aucuneconnection.mp3")

def poidsbas():
    os.system("mpg123 -q "+chem+"/poidbas.mp3")
                                                                #Questionnaire
def avezvousdesdouleurs():
    os.system("mpg123 -q "+chem+"/avezvousdesdouleurs.mp3")
def oui():
    os.system("mpg123 -q "+chem+"/reponseoui.mp3")
def non():
    os.system("mpg123 -q "+chem+"/reponsenon.mp3")
def quelleintensite():
    os.system("mpg123 -q "+chem+"/quelleintensite.mp3")
def quellelocalisation():
    os.system("mpg123 -q "+chem+"/quellelocalisation.mp3")
def quelleaction():
    os.system("mpg123 -q "+chem+"/quelleaction.mp3")
def quelleressenti():
    os.system("mpg123 -q "+chem+"/quelleressenti.mp3")
def nulpar():
    os.system("mpg123 -q "+chem+"/nulpart.mp3")
def tete():
    os.system("mpg123 -q "+chem+"/tete.mp3")
def jambe():
    os.system("mpg123 -q "+chem+"/jambe.mp3")
def bras():
    os.system("mpg123 -q "+chem+"/bras.mp3")
def abdomen():
    os.system("mpg123 -q "+chem+"/abdomen.mp3")
def autre():
    os.system("mpg123 -q "+chem+"/autre.mp3")
def bien():
    os.system("mpg123 -q "+chem+"/bien.mp3")
def fatigue():
    os.system("mpg123 -q "+chem+"/fatigue.mp3")
def triste():
    os.system("mpg123 -q "+chem+"/triste.mp3")
def heureux():
    os.system("mpg123 -q "+chem+"/heureuse.mp3")
def centre():
    os.system("mpg123 -q "+chem+"/appelcentre.mp3")
def medecin():
    os.system("mpg123 -q "+chem+"/appelmedecin.mp3")
def finquestionnaire():
    os.system("mpg123 -q "+chem+"/finquestionnaire.mp3")
