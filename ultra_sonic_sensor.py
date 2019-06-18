
import RPi.GPIO as gpio
import time

gpio.setwarnings (False)
gpio.setmode(gpio.BOARD)

trigpin = 10
echopin = 12

gpio.setup(trigpin,gpio.OUT)
gpio.setup(echopin,gpio.IN)

print ("calculate the distance")

while True:
    gpio.output(trigpin,0)
    time.sleep(2)

    gpio.output(trigpin,1)
    time.sleep (0.00001) # delay
    gpio.output(trigpin,0)

    while (gpio.input(echopin) == 0):
        start_time = time.time()

    while (gpio.input(echopin)==1):
        stop_time = time.time()

    duration = stop_time - start_time
    # speed of sound = 340m/sec = 34000 cm/sec
    distance = (34000*duration)/2 # cm/sec

    if (distance > 0) and (distance < 400):
        print ("obstacle found at a distance :",str(distance))

    else:
        print ("out of range")
