import math

class Projectile:

    """
    :parameter yMax is the maximum height of the path of the projectile
    :parameter yGoal is the height of the goal
    """
    def __init__(self, yMax, yGoal):
        self.yMax = yMax
        self.yFall = yMax - yGoal

    """
    :return a tuple (x, y) of cartesian coordinates
    """
    @staticmethod
    def toCartesian(distance, angle):
        return (distance * math.cos(angle), distance * math.sin(angle))
