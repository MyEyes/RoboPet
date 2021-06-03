from locomotion import Locomotion
import time
import config
from sensor import Sensor

loco = Locomotion()
sense = Sensor(config.SENSOR1_TRIGGER, config.SENSOR1_ECHO, config.SENSOR1_MAXDIST)
senseL = Sensor(config.SENSOR_L_TRIGGER, config.SENSOR_L_ECHO, config.SENSOR_L_MAXDIST)
senseR = Sensor(config.SENSOR_R_TRIGGER, config.SENSOR_R_ECHO, config.SENSOR_R_MAXDIST)

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
        print(senseL.measure(), sense.measure(), senseR.measure())
    time.sleep(0.5)
    loco.stop()