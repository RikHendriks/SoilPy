from .soil import *

class SoilManager:
    """
    Soil manager class.
    """

    def __init__(self):
        self.soil_layer_list = []

    # Add checks, such that the soil layer is under the previous one
    def add_soil_layer(self, s_l):
        # If s_l is a soil layer
        if isinstance(s_l, SoilLayer):
            # If the water level is above the soil layer and it is the first layer added, then add it to the list as a layer
            if s_l.water_layer.level > s_l.top_level and len(self.soil_layer_list) is 0:
                self.soil_layer_list.append(SoilLayer(Soil(10, 10), s_l.water_layer, s_l.water_layer.level, s_l.top_level))
            # If the water level is in the soil layer, then split it into two parts
            if s_l.water_layer.level < s_l.top_level and s_l.water_layer.level > s_l.bottom_level:
                # Top soil layer
                self.soil_layer_list.append(SoilLayer(s_l.soil, s_l.water_layer, s_l.top_level, s_l.water_layer.level))
                # Bottom soil layer
                self.soil_layer_list.append(SoilLayer(s_l.soil, s_l.water_layer, s_l.water_layer.level, s_l.bottom_level))
            else:
                self.soil_layer_list.append(s_l)

    def process_function(self, func, data):
        """
        Applies func to each soil layer with a given data structure that is passed along.

        :param func:
        :param data:
        :return:
        """
        for i in range(0, len(self.soil_layer_list)):
            func(self.soil_layer_list[i], data, i)