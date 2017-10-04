import numpy as np

from .soil import *


class SoilLayer(Soil):
    """
    Soil layer data class.
    """

    def __init__(self, s, wl, t, b, hc=0):
        """
        Initializes the soil layer class.

        :param s: soil class
        :param wl: water level
        :param t: top of the layer
        :param b: bottom of the layer
        :param hc: capillary_rise
        """
        self.soil = s
        self.water_layer = wl
        self.top_level = t
        self.bottom_level = b
        self.thickness = t - b
        self.capillary_rise = hc