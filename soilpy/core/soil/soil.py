class Soil:
    """
    Soil data class.
    """

    def __init__(self, g, gS):
        self.gamma = g
        self.gamma_saturated = gS