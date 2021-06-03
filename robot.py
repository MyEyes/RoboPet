from locomotion import Locomotion
from sensor import Sensor
import config
import time

MIN_DIST = 0.2

def robot_run():
    locomotion = Locomotion()
    sensor = Sensor(config.SENSOR1_TRIGGER, config.SENSOR1_ECHO, config.SENSOR1_MAXDIST)
    while True:
        dist = sensor.measure()
        while dist and dist > MIN_DIST:
            locomotion.forward(0.7)
            dist = sensor.measure()
        locomotion.stop()
        maxDist = dist
        while dist and dist < 1:
            locomotion.tightRight(0.7)
            time.sleep(0.1)
            locomotion.stop()
            dist = sensor.measure()
            if dist and dist>maxDist:
                maxDist = dist

if __name__ == "__main__":
    robot_run()