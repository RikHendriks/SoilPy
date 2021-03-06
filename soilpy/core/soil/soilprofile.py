from soilpy.core.soil import *
import math


class SoilProfile:
    """
    Soil manager class.
    """

    def __init__(self, s_p_c='n'):
        self.soil_layer_list = []
        self.soil_pressure_coefficient = s_p_c

    # Add checks, such that the soil layer is under the previous one
    def add_soil_layer(self, s_l):
        # If s_l is a soil layer
        if isinstance(s_l, SoilLayer):
            # If the water level is above the soil layer and it is the first layer added, then add it to the list as a layer
            if s_l.water_layer.level > s_l.top_level and len(self.soil_layer_list) is 0:
                self.soil_layer_list.append(SoilLayer(Soil(10, 10, 0), s_l.water_layer, s_l.water_layer.level, s_l.top_level))
            # If the water level is in the soil layer, then split it into two parts
            if s_l.water_layer.level < s_l.top_level and s_l.water_layer.level > s_l.bottom_level:
                # Top soil layer
                self.soil_layer_list.append(SoilLayer(s_l.soil, s_l.water_layer, s_l.top_level, s_l.water_layer.level))
                # Bottom soil layer
                self.soil_layer_list.append(SoilLayer(s_l.soil, s_l.water_layer, s_l.water_layer.level, s_l.bottom_level))
            else:
                self.soil_layer_list.append(s_l)

    # TODO change the name of the soil angle
    def calculate_soil_pressure_coefficient(self, a):
        """
        Calculate the soil pressure coefficient of the soil.

        :param a:
        :return:
        """
        if self.soil_pressure_coefficient == "a":
            return math.pow(math.tan(((45 - (a / 2))/180) * math.pi), 2)
        elif self.soil_pressure_coefficient == "p":
            return math.pow(math.tan(((45 - (a / 2))/180) * math.pi), 2)
        elif self.soil_pressure_coefficient == "n":
            return 1. - math.sin(((a) / 180) * math.pi)
        else:
            print("ERROR, soil pressure coefficient is not defined!")