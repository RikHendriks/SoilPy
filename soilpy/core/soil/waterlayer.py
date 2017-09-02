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