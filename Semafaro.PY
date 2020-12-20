import RPi.GPIO as GPIO
import time
Vermelho = 23
Amarelo = 24
Verde = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Vermelho,GPIO.OUT)
GPIO.setup(Amarelo,GPIO.OUT)
GPIO.setup(Verde,GPIO.OUT)

GPIO.output(Vermelho,0)
GPIO.output(Amarelo,0)
GPIO.output(Verde,0)

try:
    while True:
        GPIO.output(Verde,1)
        GPIO.output(Vermelho,0)
        time.sleep(5.0)
        
        GPIO.output(Amarelo,1)
        GPIO.output(Verde,0)
        time.sleep(1.0)



        GPIO.output(Amarelo,0)
        GPIO.output(Vermelho,1)
        time.sleep(1.5)
        
except KeyboardInterrupt:
            GPIO.cleanup()
