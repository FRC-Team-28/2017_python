class pid:

    def __init__(self, kP, kI, kD, setpoint):
        self.kP = kP
        self.kI = kI
        self.kD = kD
        self.setpoint = setpoint
        self.integral = 0.0
        self.derivative = 0.0
        self.prevError = 0.0
        self.error = 0.0

    def setPoint(self, setpoint):
        self.setpoint = setpoint

    def getPoint(self):
        return self.setpoint

    def update(self, processVariable):
        self.prevError = self.error
        self.error = self.setpoint - self.processVariable
        self.integral = self.integral + self.error
        return self.kP * self.error + self.kI * self.integral + self.kD * (self.error - self.prevError)
