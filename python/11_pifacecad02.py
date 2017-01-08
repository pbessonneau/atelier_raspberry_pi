import pifacecad
import time

def update_pin_text(event):
	cad.lcd.clear()   
	 
	pin = event.pin_num + 0

	cad.lcd.set_cursor(1, 1)        
	cad.lcd.write(pin)
	sleep(0.5)
	
	return()    

listener = pifacecad.SwitchEventListener(chip=cad)

for i in range(8):
	listener.register(i, pifacecad.IODIR_FALLING_EDGE, update_pin_text)

listener.activate()

while True:
	try:
		pass
	except:
		break
