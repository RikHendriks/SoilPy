class WaterLayer():
    """
    Water layer class.
    """
    def __init__(self, l, g=10):
        """
        Initializes the water layer class

        :param l: the level of the water layer
        :param g: the volumetric weight of water
        """
        self.level = l
        self.gamma = g

    def water_pressure(self, gl, cr=False):
        """
        Calculates the water level at a given level.

        :param gl: the level at which the water pressure needs to be calculated
        :param cr: if there is a capillary rise
        :return: returns the pressure of the water
        """
        if cr :
            return self.gamma * (gl - self.level)
        else:
            return  min(0, self.gamma * (gl - self.level))