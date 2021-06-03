from locomotion import Locomotion
from sensor import Sensor
import config
import time

def robot_run():
    locomotion = Locomotion()
    sensor = Sensor(config.SENSOR1_TRIGGER, config.SENSOR1_ECHO, config.SENSOR1_MAXDIST)
    while True:
        dist = sensor.measure()
        while dist>0.1:
            locomotion.forward(0.7)
            dist = sensor.measure()
        locomotion.stop()
        maxDist = dist
        while dist < 1:
            locomotion.tightRight()
            time.sleep(0.1)
            locomotion.stop()
            dist = sensor.measure()
            if dist>maxDist:
                maxDist = dist

if __file__ == "__main__":
    robot_run()