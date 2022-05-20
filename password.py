import time
from grovepi import *
from grove_rgb_lcd import *

potar = 2
ecran = 1
button_valid = 2

code = 0
txtPos = 0
mdp = [6,1,4,0]
mdp_en_cours = []
mdp_trouve = False

pinMode(potar, "INPUT")
pinMode(ecran, "OUTPUT")
pinMode(button_valid, "INPUT")
time.sleep(1)

setRGB(255,255,255)

while mdp_trouve == False:

    setText_norefresh("****")
    
    while txtPos < 4 :
        
        setCursor(txtPos,0)
        
        while digitalRead(button_valid) == 0:
            
            potar_value = analogRead(potar)

            if potar_value <= 1023 and potar_value >= 920.8:
                    code = 9
            elif potar_value <= 920.7 and potar_value >= 818.5:
                    code = 8
            elif potar_value <= 818.4 and potar_value >= 716.2:
                    code = 7
            elif potar_value <= 716.1 and potar_value >= 613.9:
                    code = 6
            elif potar_value <= 613.8 and potar_value >= 511.6:
                    code = 5
            elif potar_value <= 511.5 and potar_value >= 409.3:
                    code =4
            elif potar_value <= 409.2 and potar_value >= 307:
                    code = 3
            elif potar_value <= 306.9 and potar_value >= 204.7:
                    code = 2
            elif potar_value <= 204.6 and potar_value >= 102.4:
                    code = 1
            elif potar_value <= 102.3 and potar_value >= 0:
                    code = 0
            
            setText_norefresh(str(code))

        mdp_en_cours.append(code)
        txtPos += 1

    if mdp == mdp_en_cours :
            
            mdp_trouve = True
    else:
            
            setCursor(0,0)
            setRGB(255,0,0)
            setText_norefresh("Code non valide")
            time.sleep(5)

if mdp_trouve == True:
    
    setCursor(0,0)
    setRGB(0,255,0)
    setText_norefresh("Code Valide")
