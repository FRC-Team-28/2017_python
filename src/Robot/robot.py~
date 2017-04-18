import wpilib as wp


class Robot2017(wp.IterativeRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.pot = wp.AnalogInput(0)
        self.led = wp.DigitalOutput(0)
        self.led.enablePWM(self.pot.getVoltage() / 5)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.auto_loop_counter = 0  # 1 loop = 20 ms

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        pass

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.led.updateDutyCycle(self.pot.getVoltage() / 5)

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wp.LiveWindow.run()


if __name__ == "__main__":
    wp.run(Robot2017)