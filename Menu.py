from grovepi import *
from grove_rgb_lcd import *
import password
import time

potar = 2
ecran = 1
button_valid = 2

pinMode(potar, "INPUT")
pinMode(ecran, "OUTPUT")
pinMode(button_valid, "INPUT")

alarme = False
etat_ecran = 0
etat_ecran_int = False

while potar >=0:
  if alarme == False:
    setRGB(255,0,0)
    setText_noresfresh("Alarme : OFF")
  else:
      setRGB(0,255,0)
      setText_noresfresh("Alarme : ON")

  if etat_ecran == 0 and etat_ecran_int == False:
    #while
    if digitalRead(button_valid) == 1:
      etat_ecran_int = True
      time.sleep(1)
      if alarme == False:
        setRGB(255,255,255)
        setText_norefresh("Activer alarme ?")
        #while
        if digitalRead(button_valid) == 1:
          time.sleep(1)
          password
          time.sleep(2)
          alarme = True
      else:
        setRGB(255,255,255)
        setText_norefresh("Desactiver alarme ?")
        #while
        if digitalRead(button_valid) == 1:
          time.sleep(1)
          password
          time.sleep(2)
          alarme = False

        
        
        
