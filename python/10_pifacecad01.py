import pifacecad
import time
import netifaces as ni

# Trouver l'adresse IP
ni.ifaddresses('eth0')
ip = ni.ifaddresses('eth0')[2][0]['addr']

# Allumer le PiFace
cad = pifacecad.PiFaceCAD()
cad.lcd.backlight_on()
cad.lcd.clear()

# Afficher au premier caractère sur la première ligne
cad.lcd.set_cursor(1, 0)        
cad.lcd.write(`Hello World')

cad.lcd.set_cursor(1, 1)        
cad.lcd.write(ip)

sleep(5)

cad.lcd.backlight_off()