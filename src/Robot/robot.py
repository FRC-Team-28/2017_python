import wpilib
import drive


class Robot2017(wpilib.IterativeRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        pass

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.auto_loop_counter = 0  # 1 loop = 20 ms

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        pass

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        pass

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()


if __name__ == "__main__":
    wpilib.run(Robot2017)