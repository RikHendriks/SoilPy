from .soil import  *


class SoilMechanicsData():
    """
    The soil mechanics data class
    """

    def __init__(self):
        self.water_pressure_list = []
        self.vertical_normal_stress_list = []
        self.effective_vertical_normal_stress_list = []

    def __str__(self):
        output = "Water pressure: " + str(self.water_pressure_list) + "\n"
        output += "Vertical normal stress: " + str(self.vertical_normal_stress_list) + "\n"
        output += "Effective vertical normal stress: " + str(self.effective_vertical_normal_stress_list)
        return output


def calculate_water_pressure(s_l, data, i):
    """
    Calculates the water pressure.

    :param s_l:
    :param data:
    :return:
    """
    # Output variables
    output = [0, 0]
    # Calculate the water pressure for the bottom and top level
    # If the water level is above the top level of the soil layer
    if s_l.water_layer.level + s_l.capillary_rise >= s_l.top_level:
        output[0] = s_l.water_layer.gamma * (s_l.water_layer.level - s_l.top_level)
        output[1] = s_l.water_layer.gamma * (s_l.water_layer.level - s_l.bottom_level)
    # Add the output to the water pressure list
    data.water_pressure_list.append(output)


# TODO reminder: add the vertical pressure on top of the first soil layer after this calculation is done
def calculate_vertical_normal_stress(s_l, data, i):
    """
    Calculates the vertical normal stress.

    :param s_l:
    :param data:
    :return:
    """
    # Output variables
    output = [0, 0]
    # Calculate the vertical normal stress for the bottom and top level.
    # If it is not the first layer
    if i is not 0:
        output[0] = data.vertical_normal_stress_list[i - 1][1]
    # If the soil is saturated or not
    if s_l.water_layer.level + s_l.capillary_rise >= s_l.top_level:
        output[1] = output[0] + s_l.thickness * s_l.soil.gamma_saturated
    else:
        output[1] = output[0] + s_l.thickness * s_l.soil.gamma
    # Add the output to the vertical normal stress list
    data.vertical_normal_stress_list.append(output)


def calculate_effective_vertical_normal_stress(s_l, data, i):
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
    output[0] = data.vertical_normal_stress_list[i][0] - data.water_pressure_list[i][0]
    # Bottom
    output[1] = data.vertical_normal_stress_list[i][1] - data.water_pressure_list[i][1]
    # Add the output to the effective vertical normal stress list
    data.effective_vertical_normal_stress_list.append(output)