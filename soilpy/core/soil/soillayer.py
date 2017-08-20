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
        self.depth = t - b
        self.capillary_rise = hc

    def vertical_normal_stress(self, level):
        #ToDo add a parameter to add the pressure from a layer above.
        """
        Returns the vertical normal stress.

        :param level: the level at which the stress is to be determined.
        :return: returns the stress tensor of the soil layer at point d, Stress2D class.
        """
        # If level is higher than the water level.
        if level <= self.top_level and level >= self.bottom_level:
            # If level is higher then the water level.
            if level > self.water_layer.level:
                return self.soil.gamma * (level - self.top_level)
            # If level is lower then the water level.
            else:
                #If the water level is between the top and the bottom level, then apply the gamma first and then the gamma saturated.
                if self.water_layer.level <= self.top_level:
                    return self.soil.gamma * (self.water_layer.level - self.top_level) + self.soil.gamma_saturated * (level - self.water_layer.level)
                else:
                    return self.soil.gamma_saturated * (level - self.top_level)
        else:
            raise ValueError("The given level=" + str(level) + " is not between the top level t=" + str(
                self.top_level) + " and the bottom level b=" + str(self.bottom_level))

    def vertical_water_pressure(self, level, water_level_soil_layer_below=None):
        #ToDo change this function such that it needs an input of the vert normal stress and the water pressure above it.
        #ToDo add a function for the water pressure of layers that are not hydrostatic.
        """
        Returns the vertical water pressure.

        :param level:
        :param water_level_soil_layer_below:
        :return:
        """
        # If level is higher than the water level.
        if level <= self.top_level and level >= self.bottom_level:
            # If the water level in the soil layer below this one is not none then set it to the water level of the current one.
            if water_level_soil_layer_below is None:
                water_level_soil_layer_below = self.water_layer
            # If level is higher then the water level.
            if level > self.water_layer.level:
                return 0
            else:
                # Determine if the water layer is in our outide the soil layer
                top_level = min(self.water_layer.level, self.top_level)
                # Calculate the top water pressure.
                top_water_pressure = self.water_layer.water_pressure(self.top_level)
                # Calculate the bottom water pressure.
                bottom_water_pressure = water_level_soil_layer_below.water_pressure(self.bottom_level)
                # Lerp the level between the top and bottom water pressures.
                return ((level - top_level) / (self.bottom_level - top_level)) * (bottom_water_pressure - top_water_pressure)
        else:
            raise ValueError("The given level=" + str(level) + " is not between the top level t=" + str(
                self.top_level) + " and the bottom level b=" + str(self.bottom_level))


    def effective_vertical_normal_stress(self, level):
        # ToDo Add support for clay layers which have variable water pressures from the laer above and below it.
        """
        Returns the effective vertical normal stress.

        :param level:
        :return:
        """




    def stress_tensor(self, level):
        """
        Returns the stress tensor at the given level.

        :param level: the level at which the tensor is calculated.
        :return: returns the stress tensor of the soil layer at point d, Stress2D class.
        """

    def effective_stress_tensor(self, level):
        """
        Returns the effective stress tensor at the given level.

        :param level: the level at which the tensor is calculated.
        :return: returns the stress tensor of the soil layer at point d, Stress2D class.
        """

