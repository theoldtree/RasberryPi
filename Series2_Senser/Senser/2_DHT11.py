import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D18)

while True:
    try: 
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print(temperature, humidity)
        time.sleep(2.0)
    except KeyboardInterrupt:
        pass
        print("Terminated by Keyboard")
        GPIO.cleanup()
        exit()
                                            