import Rpi.GPIO as GPIO
import time

# Activer la bonne numérotation des pins
GPIO.setmode(GPIO.BCM)

# Si la diode est branché sur la pin 18.
# 1) activer la broche en sortie de courant
GPIO.setup(18, GPIO.OUT)
# 2) activer la diode
GPIO.output(18, GPIO.HIGH)

# Attendre 2 secondes
time.sleep(2)

# Eteindre la diode
GPIO.output(18, GPIO.LOW)