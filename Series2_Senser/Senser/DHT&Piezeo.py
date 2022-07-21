import RPi.GPIO as GPIO
from time import sleep
import board
import adafruit_dht

GPIO.cleanup()
GPIO.setwarnings(False)
dhtDevice = adafruit_dht.DHT11(board.D18)

GPIO.setmode(GPIO.BCM)
buzzer = 17
scale = 261
GPIO.setup(buzzer,GPIO.OUT)
p = GPIO.PWM(buzzer, 600)

try: 
    p.ChangeFrequency(scale)
    temperature = dhtDevice.temperature
    humidity = dhtDevice.humidity
    print(temperature, humidity)
    if (temperature > 23):
        GPIO.ouput(buzzer,HIGH)
    time.sleep(2.0)
except KeyboardInterrupt:
    pass
    print("Terminated by Keyboard")
    GPIO.cleanup()
    exit()