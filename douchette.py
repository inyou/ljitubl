#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : 5.0.0
from evdev import InputDevice, ecodes, list_devices, categorize
import signal, sys
import time
import os
import urllib2
import ultra
import config
import speech
alarmeon=False
reponses=[0,0,[0,0,0,0,0],[0,0],[0,0,0,0]]
ala_nb=""
ques=False
numques=0
qpose=False
ufon=False
uf_nb=0
sign=+1
configurable=False
os.system("amixer cset numid=1 -- "+str(config.volumeson)+"%")
scancodes = {
    # Scancode: ASCIICode
    0: None, 1: u'ESC', 2: u'&', 3: u'é', 4: u'\"', 5: u'\'', 6: u'(', 7: u'-', 8: u'è', 9: u'_',
    10: u'ç', 11: u'à', 12: u')', 13: u'=', 14: u'BKSP', 15: u'TAB', 16: u'a', 17: u'z', 18: u'e', 19: u'r',
    20: u't', 21: u'y', 22: u'u', 23: u'i', 24: u'o', 25: u'p', 26: u'^', 27: u'$', 28: u'CRLF', 29: u'LCTRL',
    30: u'q', 31: u's', 32: u'd', 33: u'f', 34: u'g', 35: u'h', 36: u'j', 37: u'k', 38: u'l', 39: u'm',
    40: u'ù', 41: u'*', 42: u'LSHFT', 43: u'<', 44: u'w', 45: u'x', 46: u'c', 47: u'v', 48: u'b', 49: u'n',
    50: u',', 51: u';', 52: u':', 53: u'!', 54: u'RSHFT', 56: u'LALT', 57: u' ', 86: u'<', 100: u'RALT',
    101: u'ESC', 102: u'1', 103: u'2', 104: u'3', 105: u'4', 106: u'5', 107: u'6', 108: u'7', 109: u'8',
    110: u'9', 111: u'0', 112: u'°', 113: u'+', 114: u'BKSP', 115: u'TAB', 116: u'A', 117: u'Z', 118: u'E', 119: u'R',
    120: u'T', 121: u'Y', 122: u'U', 123: u'I', 124: u'O', 125: u'P', 126: u'¨', 127: u'£', 128: u'CRLF', 129: u'LCTRL',
    130: u'Q', 131: u'S', 132: u'D', 133: u'F', 134: u'G', 135: u'H', 136: u'J', 137: u'K', 138: u'L', 139: u'M',
    140: u'%', 141: u'µ', 142: u'LSHFT', 143: u'>', 144: u'W', 145: u'X', 146: u'C', 147: u'V', 148: u'B', 149: u'N',
    150: u'?', 151: u'.', 152: u'/', 153: u'§', 154: u'RSHFT', 156: u'LALT', 157: u' ', 186: u'>',
    201: u'ESC', 202: u'1', 203: u'~', 204: u'#', 205: u'{', 206: u'[', 207: u'|', 208: u'`', 209: u'\\',
    210: u'^', 211: u'@', 212: u']', 213: u'}', 214: u'BKSP', 215: u'TAB', 216: u'A', 217: u'Z', 218: u'E', 219: u'R',
    220: u'T', 221: u'Y', 222: u'U', 223: u'I', 224: u'O', 225: u'P', 226: u'¨', 227: u'£', 228: u'CRLF', 229: u'LCTRL',
    230: u'Q', 231: u'S', 232: u'D', 233: u'F', 234: u'G', 235: u'H', 236: u'J', 237: u'K', 238: u'L', 239: u'M',
    240: u'%', 241: u'µ', 242: u'LSHFT', 243: u'>', 244: u'W', 245: u'X', 246: u'C', 247: u'V', 248: u'B', 249: u'N',
    250: u'?', 251: u'.', 252: u'/', 253: u'§', 254: u'RSHFT', 256: u'LALT', 257: u' ', 286: u'>', 300: u'R'
}

def signal_handler(signal, frame):
    print 'Stopping'
    boucle=False
    #dev.ungrab()
    sys.exit(0)

def test_wifi():
    print "TEST_WIFI"
    try:
        response=urllib2.urlopen('http://www.google.com',timeout=5)
        return True
    except urllib2.URLError as err:
        pass
        return False
    

#Déclaration des Thread
speech.bonjour()
thread_ultra=ultra.ultra()
boucle=True
alarmeon=False
while boucle:
    signal.signal(signal.SIGINT, signal_handler)
    barCodeDeviceString2 = "Barcode AFANDA BARCODE"
    pasdescanner=True
    print "Recherche du Scanner de code barre"
    while pasdescanner:
        devices = map(InputDevice, list_devices())
        for device in devices:
            if (device.name == barCodeDeviceString2):
                print "SCANNER USB"
                dev = InputDevice(device.fn)
                pasdescanner=False
                speech.douchecon()
                print "Scanner de code barre : OK"
    try:
        dev.grab()
    except:
        print "Erreur GRAB"
    barcode = ""
    shift=0
    try:
        for event in dev.read_loop():
            if event.type == ecodes.EV_KEY:
                data = categorize(event)
                if (data.scancode==42 or data.scancode==54):
                    if data.keystate ==1:
                        shift=100
                    else:
                        shift=0
                if (data.scancode==100):
                    if data.keystate ==1:
                        shift=200
                    else:                    
                        shift=0
                if data.keystate == 1 and data.scancode != 42 and data.scancode!=54 and data.scancode!=100:#  Catch only keydown, and not Enter
                    if data.scancode == 28:
                        print barcode
                        #Commande de la douchette
                                                                            #TEST WIFI
                        if (barcode=="WIFI"):
                            if (test_wifi()):
                                speech.connectionactive()
                            else :
                                speech.aucuneconnection()
                                                                            #REVERSE SSH
                        if (barcode=="HELP"):
                            print "HELP"
                            os.system(config.repertoire_origine+"tunnel.py &");
                                                                            #ALARME
                        if (barcode=="SS:00:00:27") or alarmeon==True:
                            alarmeon=True
                            U=["U0","U1","U2","U3","U4","U5","U6","U7","U8","U9"]
                            if barcode=="SS:00:00:27":
                                print "Entrez le nombre d'alarme que vous avez eu."
                                speech.entrezalarme()
                            if (barcode in U):
                                ala_nb=ala_nb+barcode[1]
                                print ala_nb
                                speech.say_int(int(ala_nb))
                            if (barcode=="ANNULER"):
                                ala_nb=""
                                print "Entrez le nombre d'alarme que vous avez eu."
                                speech.entrezalarme()
                            if (barcode=="VALID"):
                                tim=int(time.time())
                                s=config.url+"?id="+config.boxid+"&pks="+config.pks+"&date="+str(tim)
                                s=s+"&ala="+str(int(ala_nb))
                                config.dump_objet("atsend/"+str(tim)+".ala",s)
                                ala_nb=""
                                alarmeon=False
                                speech.valider()
                                                                                #ULTRAFILTRATION
                        if (barcode=="SS:00:00:28") or ufon==True:
                            ufon=True
                            U=["U0","U1","U2","U3","U4","U5","U6","U7","U8","U9","U-"]
                            if barcode=="SS:00:00:28":
                                speech.entrezultrafiltration()
                            if (barcode in U):
                                if (barcode=="U-"):
                                    sign=-1*sign
                                    if uf_nb==0:
                                        speech.moins()
                                    else:
                                        speech.say_intneg(int(sign*uf_nb))
                                else :
                                    uf_nb=uf_nb*10+int(barcode[1])
                                    speech.say_intneg(int(sign*uf_nb))
                            if (barcode=="ANNULER"):
                                uf_nb=0
                                sign=1
                                speech.entrezultrafiltration()
                            if (barcode=="VALID"):
                                tim=int(time.time())
                                s=config.url+"?id="+config.boxid+"&pks="+config.pks+"&date="+str(tim)
                                s=s+"&ult="+str(int(sign*uf_nb))
                                config.dump_objet("atsend/"+str(tim)+".ult",s)
                                uf_nb=0
                                sign=1
                                ufon=False
                                speech.valider()
                                                                                #questionnaire
                        if (barcode=="ques"):
                            ques=True
                            qpose=True
                        if ques:
                            print reponses
                            if barcode=="oui" and numques==0:
                                speech.oui()
                                reponses[0]=1
                            if barcode=="non" and numques==0:
                                speech.non()
                                reponses[0]=0
                            if barcode[0]=="d" and numques==1:
                                speech.say_int(int(barcode[1:]))
                                reponses[1]=int(barcode[1:])
                            if barcode=="tete" and numques==2:
                                speech.tete()
                                reponses[2][0]=1
                            if barcode=="bras" and numques==2:
                                speech.bras()
                                reponses[2][1]=1
                            if barcode=="abdomen" and numques==2:
                                speech.abdomen()
                                reponses[2][2]=1
                            if barcode=="jambe" and numques==2:
                                speech.jambe()
                                reponses[2][3]=1
                            if barcode=="autre" and numques==2:
                                speech.autre()
                                reponses[2][4]=1
                            if barcode=="nulpar" and numques==2:
                                speech.nulpar()
                                reponses[2]=[0,0,0,0,0]
                            if barcode=="centre" and numques==3:
                                speech.centre()
                                reponses[3][0]=1
                            if barcode=="medcin" and numques==3:
                                speech.medecin()
                                reponses[3][1]=1
                            if barcode=="bien" and numques==4:
                                speech.bien()
                                reponses[4][0]=1
                            if barcode=="triste" and numques==4:
                                speech.triste()
                                reponses[4][1]=1
                            if barcode=="fatigue" and numques==4:
                                speech.fatigue()
                                reponses[4][2]=1
                            if barcode=="heureux" and numques==4:
                                speech.heureux()
                                reponses[4][3]=1
                            if barcode=="VALID":
                                speech.valider()
                                qpose=True
                                numques=numques+1
                                print "REPONSE : ",reponses
                                if numques==5:
                                    print "FIN de QUESTIONNAIRE J'ENVOIS"
                                    tim=int(time.time())
                                    s=config.url+"?id="+config.boxid+"&pks="+config.pks+"&date="+str(tim)
                                    s=s+"&quest="+str(reponses[0])+str(hex(reponses[1]))[2:]+str(reponses[2][0])+str(reponses[2][1])+str(reponses[2][2])+str(reponses[2][3])+str(reponses[2][4])+str(reponses[3][0])+str(reponses[3][1])+str(reponses[4][0])+str(reponses[4][1])+str(reponses[4][2])+str(reponses[4][3])
                                    config.dump_objet("atsend/"+str(tim)+".ques",s)
                                    print s
                                    speech.finquestionnaire()
                                    #reinit question
                                    qpose=False
                                    numques=0
                                    ques=False
                                    reponses=[0,0,[0,0,0,0,0],[0,0],[0,0,0,0]]
                            if numques==0 and qpose:
                                speech.avezvousdesdouleurs()
                                qpose=False
                            if numques==1 and qpose:
                                speech.quelleintensite()
                                qpose=False
                            if numques==2 and qpose:
                                speech.quellelocalisation()
                                qpose=False
                            if numques==3 and qpose:
                                speech.quelleaction()
                                qpose=False
                            if numques==4 and qpose:
                                speech.quelleressenti()
                                qpose=False
                            
                                                                                #CONFIGURATION ID/PKS/PORT SSH
                        if barcode=="SS:00:00:07":
                            speech.redemarrage()
                            os.system("sudo reboot")
                        if (barcode[0:2]=="ID"):
                            print "configuration ID"
                            config.boxid=barcode[2:]
                            config.error=0
                            config.err_res=0
                            config.reboot=0
                            config.cycle=0
                            os.system("rm "+config.repertoire_origine+"atsend/*")
                            os.system("rm "+config.repertoire_origine+"sent/*")
                            config.save_config()
                        if (barcode[0:3]=="PKS"):
                            print "configuration PKS"
                            config.pks=barcode[3:]
                            config.save_config()
                        if (barcode[0:3]=="SSH"):
                            print "configuration port SSH"
                            config.port=int(barcode[3:])
                            config.save_config()
                                                                                #POCHES
                        if (barcode in ["P1","P2","P3","P4","P5","P6","P7","P8"])and(thread_ultra.isrunning()==False):
                            thread_ultra=ultra.ultra()
                            print "poche "+str(int(barcode[1]))
                            thread_ultra.settype(int(barcode[1]))
                            thread_ultra.start()
                        if (barcode=="STOP")and(thread_ultra.isrunning()):
                            thread_ultra.stop()
                            speech.annulation()
                                                                                #AIDE
                        if barcode=="aide01":
                           speech.presentation()
                        if barcode=="aide02":
                           speech.installation()
                        if barcode=="aide03":
                           speech.aidetensiometre()
                        if barcode=="aide04":
                           speech.aidethemperature()
                        if barcode=="aide05":
                           speech.aidebalance()
                        if barcode=="aide06":
                           speech.aidepoche()
                        if barcode=="aide07":
                           speech.problemetechnique()
                        if barcode=="aide08":
                           speech.problememedical()
                                                                                #VOLUME SON
                        if barcode=="SS:00:00:0D":
                            print config.volumeson
                            if (config.volumeson<100):
                                config.volumeson=config.volumeson+5
                            os.system("amixer cset numid=1 -- "+str(config.volumeson)+"%")
                            speech.sonplus()
                        if barcode=="SS:00:00:0E":
                            print config.volumeson
                            if (config.volumeson>80):
                                config.volumeson=config.volumeson-5
                                config.save_config()
                            os.system("amixer cset numid=1 -- "+str(config.volumeson)+"%")
                            speech.sonmoins()
                        barcode = ""
                    else:
                        barcode += scancodes[shift+data.scancode]
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args      # arguments stored in .args
        print inst           # __str__ allows args to be printed directly
        try:
            dev.ungrab()
        except:
            print "Erreur UNGRAB"
        print "déconnexion du scanner de code bar"
        speech.douchedecon()