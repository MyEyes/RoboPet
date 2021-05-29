from locomotion import Locomotion
import time
import config
from sensor import Sensor

loco = Locomotion()
sense = Sensor(config.SENSOR1_TRIGGER, config.SENSOR1_ECHO, config.SENSOR1_MAXDIST)
result = ""

try:
    while True:
        loco.tightLeft()
        time.sleep(0.01)
        loco.stop()
        time.sleep(0.2)
        dist = sense.measure()
        print(dist)
        result +=","
        result += str(dist)
except:
    print(result)