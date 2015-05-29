import explorerhat
from time import sleep
from random import randint

def wheel(channel, event):
    explorerhat.light.blink(0.5,0.5)
    for i in range(5):
        duration = randint(1,10)
    print(duration)
    explorerhat.motor.one.forward(100)
    sleep(duration)
    explorerhat.motor.one.stop()
    explorerhat.light.off()


explorerhat.touch.one.pressed(wheel)
  
