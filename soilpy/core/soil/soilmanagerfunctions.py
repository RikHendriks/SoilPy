from .soil import  *

class SoilMechanicsData():
    """
    The soil mechanics data class
    """

    def __init__(self):
        self.vertical_normal_stress_list = LevelList()
        self.effective_vertical_normal_stress_list = LevelList()
        self.water_pressure_list = LevelList()


class LevelList():
    """
    The level list class
    """

    def __init__(self):
        self.level_list = []
        self.top_level = 0
        self.bottom_level = 0

    def add_level_value(self, level, value):
        # If level list is empty
        if self.level_list is []:
            self.level_list += [level, value]
            self.top_level = level
            self.bottom_level = level
        else:
            b = True
            # For each level value in the level list
            for i in range(0, len(self.level_list)):
                # If the level is greater then the level in the list at i
                if level > self.level_list[i]:
                    self.level_list.insert(i, [level, value])
                    # If it is the topmost level
                    if i == 0:
                        self.top_level = level
                    b = False
                    break
            # If it is the last level
            if b:
                self.level_list += [level, value]
                self.bottom_level = level



def calculate_water_pressure(s_l, data):
    """
    Calculates the water pressure.

    :param s_l:
    :param data:
    :return:
    """
    # Output variables
    output = [0, 0]
    # Calculate the water pressure for the bottom and top level
    # Bottom
    if s_l.water_layer.level + s_l.capillary_rise > s_l.bottom_level:
        output[1] = s_l.water_layer.gamma * (s_l.bottom_level - s_l.water_layer.level)
        # Top
        if s_l.water_layer.level + s_l.capillary_rise > s_l.top_level:
            output[0] = s_l.water_layer.gamma * (s_l.top_level - s_l.water_layer.level)
    # Add the output to the water pressure list
    # TODO add the necessary level values
    data.water_pressure_list.add_level_value(output[0], output[1])


def calculate_vertical_normal_stress(s_l, data):
    """
    Calculates the vertical normal stress.

    :param s_l:
    :param data:
    :return:
    """
    # Output variables
    output = [0, 0]
    # Calculate the vertical normal stress for the bottom and top level.
    # TODO add the calculation for the vertical normal stress
    # Add the output to the vertical normal stress list
    # TODO add the necessary level values
    data.vertical_normal_stress.add_level_value(output[0], output[1])


def calculate_effective_vertical_normal_stress(s_l, data):
    """
    Calculates the effective vertical normal stress.

    :param s_l:
    :param data:
    :return:
    """
    # Output variables
    output = [0, 0]
    # Calculate the effective vertical normal stress for the bottom and top level.
    # Top
    output[0] = data.vertical_normal_stress[0] - data.water_pressure_list[0]
    # Bottom
    output[1] = data.vertical_normal_stress[1] - data.water_pressure_list[1]
    # Add the output to the effective vertical normal stress list
    # TODO add the necessary level values
    data.effective_vertical_normal_stress.add_level_value(output[0], output[1])