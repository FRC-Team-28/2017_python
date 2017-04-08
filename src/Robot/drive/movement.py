import wpilib

class Movement:

    def __init__(self):
        pass  # TODO

    def getHeader(self):
        pass  # TODO

    def setHeader(self, header):
        pass  # TODO

    """
    param x: positive x velocity is robot starboard
    param y: positive y velocity is robot fore
    param rotation: positive rotation is clockwise when viewed from above
    """
    def robotCentric(self, x, y, rotation):
        pass  # TODO

    """
    param x: positive x velocity is field right
    param y: positive y velocity is field forward
    param rotation: positive rotation is clockwise when viewed from above
    """
    def fieldCentric(self, x, y, rotation):
        pass # TODO