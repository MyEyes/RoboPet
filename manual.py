from locomotion import Locomotion
import time

loco = Locomotion()

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
    time.sleep(0.5)
    loco.stop()