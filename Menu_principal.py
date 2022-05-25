from grovepi import *
from grove_rgb_lcd import *
import password2
import time

potar = 2
ecran = 1
button_valid = 2

Bipper_Alarme = 3
Mem_presence = 0
Capteur_presence = 4

Temp = 7

pinMode(Bipper_Alarme,"OUTPUT")
pinMode(Capteur_presence,"INPUT")

pinMode(Temp, "INPUT")

pinMode(potar, "INPUT")
pinMode(ecran, "OUTPUT")
pinMode(button_valid, "INPUT")

alarme = False
etat_ecran = 0
etat_ecran_int = False

while potar >=0:

        if potar <= 512:  

              etat_ecran_int = False
              if alarme == False:
                      setRGB(255,0,0)
                      setText_norefresh("Alarme : OFF")
              else:
                      setRGB(0,255,0)
                      setText_norefresh("Alarme : ON")

              if etat_ecran == 0 and etat_ecran_int == False:
                      if digitalRead(button_valid) == 1:
                              etat_ecran_int = True
                              time.sleep(1)
                              if alarme == False:
                                      setRGB(255,255,255)
                                      setText_norefresh("Activer alarme ?")
                                      time.sleep(4)
                                      password2.password()
                                      time.sleep(2)
                                      alarme = True
                              else:
                                      setRGB(255,255,255)
                                      setText_norefresh("Desactiver alarme ?")
                                      time.sleep(4)
                                      password2.password()
                                      time.sleep(2)
                                      alarme = False


              if alarme == True and digitalRead(Capteur_presence) == 1:

                      Mem_presence = 1
                      while Mem_presence ==1:
                              digitalWrite(Bipper_Alarme,1)
                              time.sleep(5)
                              digitalWrite(Bipper_Alarme,0)
                               Mem_presence = 0

                              
        elif potar > 512 :
          
              [T,H]=dht(Temp,0)
              now  = datetime.datetime.now()
              d, m, y, h, mn,= now.day, now.month, now.year, now.hour, now.minute

              esp=""
              txt1=str(d)+"/"+str(m)+"/"+str(y)+"       "+str(h)+":"+str(mn)+" | "+str(T)+"C"
              txt2=" Volets Fermes"
              txt3=str(d)+"/"+str(m)+"/"+str(y)+"       "+str(h)+":"+str(mn)+" | "+str(T)+"C"
              txt4="Volets Ouverts"
              txt5=str(d)+"/"+str(m)+"/"+str(y)+"       "+str(h)+":"+str(mn)+" | "+str(T)+"C"
              txt6="Volets Fermes a 50%"
              z=0

              setRGB(255,140,40)


              if h >= 20 and h <= 5:          #Il fait nuit

                      while z<=5:
                              setText_norefresh(esp + txt1)
                              time.sleep(1)
                              setText_norefresh(esp + txt2)
                              z=z+1


              elif h > 5 and h < 20:          #Il fait jour

                      if T < 22 :             #Fonction de la température intérieur

                              while z<=5:

                                      setText_norefresh(esp + txt3)
                                      time.sleep(1)
                                      setText_norefresh(esp + txt4)
                                      time.sleep(1)
                                      z=z+1

                      else :
                              while z<=5:
                                      setText_norefresh(esp + txt5)
                                      time.sleep(1)
                                      setText_norefresh(esp + txt6)
                                      time.sleep(1)
                                      z=z+1
        
