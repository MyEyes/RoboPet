import RPi.GPIO as GPIO
import time

class Sensor:
    def __init__(self, triggerpin, echopin, max_dist):
        self.trigger = triggerpin
        self.echo = echopin
        self.speed_of_sound = 343.26
        self.timeout = 2
        self.max_dist = max_dist
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.output(self.trigger, GPIO.LOW)

    def measure(self):
        GPIO.output(self.trigger, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trigger, GPIO.LOW)
        wait_start_time = time.time()

        while GPIO.input(self.echo)==0:
            pulse_start_time = time.time()
            if(pulse_start_time-wait_start_time>self.timeout):
                return None
        while GPIO.input(self.echo)==1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        dist = pulse_duration * self.speed_of_sound
        if(dist>self.max_dist):
            return None
        return dist