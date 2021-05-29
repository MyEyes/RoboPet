from locomotion import Locomotion
import time
import config
from sensor import Sensor

loco = Locomotion()
sense = Sensor(config.SENSOR1_TRIGGER, config.SENSOR1_ECHO, config.SENSOR1_MAXDIST)

while True:
    loco.tightLeft()
    time.sleep(0.01)
    loco.stop()
    print(sense.measure())