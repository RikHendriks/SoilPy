from .soil import *

class SoilManager:
    """
    Soil manager class.
    """

    def __init__(self):
        self.soil_layer_list = []

    def add_soil_layer(self, s_l):
        if isinstance(s_l, SoilLayer):
            self.soil_layer_list += s_l

    def process_function(self, func, data):
        """
        Applies func to each soil layer with a given data structure that is passed along.

        :param func:
        :param data:
        :return:
        """
        for s_l in self.soil_layer_list:
            func(s_l, data)