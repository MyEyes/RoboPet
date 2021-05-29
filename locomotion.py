import config
from gpiozero import Motor

class Locomotion:
    def __init__(self):
        self.motorR = Motor(config.MOTOR1_IN1, config.MOTOR1_IN2, enable = config.MOTOR1_EN)
        self.motorL = Motor(config.MOTOR2_IN1, config.MOTOR2_IN2, enable = config.MOTOR2_EN)

    def justifyPower(self, power):
        if power>1:
            power = 1
        if power < config.MOTOR_MIN_POWER:
            power = config.MOTOR_MIN_POWER
        return power

    def forward(self, power=1):
        power = self.justifyPower(power)
        self.motorL.forward(power)
        self.motorR.forward(power)

    def backward(self, power=1):
        power = self.justifyPower(power)
        self.motorL.backward(power)
        self.motorR.backward(power)

    def tightLeft(self, power=1):
        power = self.justifyPower(power)
        self.motorL.backward(power)
        self.motorR.forward(power)

    def tightRight(self, power=1):
        power = self.justifyPower(power)
        self.motorL.forward(power)
        self.motorR.backward(power)

    def stop(self):
        self.motorL.stop()
        self.motorR.stop()