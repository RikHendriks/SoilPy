class Soil:
    """
    Soil data class.
    """

    # TODO look up the angle name in the soil mechanics pdf
    def __init__(self, g, gS, a):
        self.gamma = g
        self.gamma_saturated = gS
        self.angle = a