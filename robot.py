from locomotion import Locomotion
from sensor import Sensor
import config
import time

MIN_DIST = 0.2

def minDist(senseL, senseC, senseR):
    distL = senseL.measure()
    distR = senseR.measure()
    distC = senseC.measure()
    if distL and distL<distR and distL<distC:
        return distL
    if distR and distR<distL and distR<distC:
        return distR
    if distC:
        return distC
    return None

def robot_run():
    locomotion = Locomotion()
    sensor = Sensor(config.SENSOR1_TRIGGER, config.SENSOR1_ECHO, config.SENSOR1_MAXDIST)
    senseL = Sensor(config.SENSOR_L_TRIGGER, config.SENSOR_L_ECHO, config.SENSOR_L_MAXDIST)
    senseR = Sensor(config.SENSOR_R_TRIGGER, config.SENSOR_R_ECHO, config.SENSOR_R_MAXDIST)
    while True:
        dist = minDist(senseL, sensor, senseR)
        while dist and dist > MIN_DIST:
            locomotion.forward(0.7)
            dist = minDist(senseL, sensor, senseR)
        locomotion.stop()

        while dist and dist < 1:

            distL = senseL.measure()
            distR = senseR.measure()
            if(distL<distR):
                locomotion.tightRight(0.7)
            else:
                locomotion.tightLeft(0.7)
            time.sleep(0.1)
            locomotion.stop()
            dist = sensor.measure()

if __name__ == "__main__":
    robot_run()