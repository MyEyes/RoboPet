from locomotion import Locomotion
import time
import config
from sensor import Sensor

loco = Locomotion()
sense = Sensor(config.SENSOR1_TRIGGER, config.SENSOR1_ECHO, config.SENSOR1_MAXDIST)

while True:
    data = input()
    if 'w' in data:
        loco.forward()
    if 'a' in data:
        loco.tightLeft()
    if 'd' in data:
        loco.tightRight()
    if 's' in data:
        loco.backward()
    if 'm' in data:
        print(sense.measure())
    time.sleep(0.5)
    loco.stop()