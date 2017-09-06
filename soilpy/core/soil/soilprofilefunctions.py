from .soil import  *


class SoilProfileData():
    """
    The soil mechanics data class
    """

    def __init__(self):
        self.level_list = []
        self.water_pressure_list = []
        self.vertical_normal_stress_list = []
        self.horizontal_normal_stress_list = []
        self.effective_vertical_normal_stress_list = []
        self.effective_horizontal_normal_stress_list = []

    def __str__(self):
        output = "Level: " + str(self.level_list) + "\n"
        output += "Water pressure: " + str(self.water_pressure_list) + "\n"
        output += "Vertical normal stress: " + str(self.vertical_normal_stress_list) + "\n"
        output += "Horizontal normal stress: " + str(self.horizontal_normal_stress_list) + "\n"
        output += "Effective vertical normal stress: " + str(self.effective_vertical_normal_stress_list) + "\n"
        output += "Effective horizontal normal stress: " + str(self.effective_horizontal_normal_stress_list)
        return output


def calculate_level(s_p, data, i):
    """
    Calculates the level.

    :param s_p:
    :param data:
    :param i:
    :return:
    """
    # Output variables
    output = [0, 0]
    # Current soillayer
    s_l = s_p.soil_layer_list[i]
    # Calculate the level for the bottom and top level
    # Top
    output[0] = s_l.top_level
    # Bottom
    output[1] = s_l.bottom_level
    # Add the output to the water pressure list
    data.level_list.append(output)


def calculate_water_pressure(s_p, data, i):
    """
    Calculates the water pressure.

    :param s_l:
    :param data:
    :return:
    """
    # Output variables
    output = [0, 0]
    # Current soillayer
    s_l = s_p.soil_layer_list[i]
    # Calculate the water pressure for the bottom and top level
    # If the water level is above the top level of the soil layer
    if s_l.water_layer.level + s_l.capillary_rise >= s_l.top_level:
        output[0] = s_l.water_layer.gamma * (s_l.water_layer.level - s_l.top_level)
        output[1] = s_l.water_layer.gamma * (s_l.water_layer.level - s_l.bottom_level)
    # Add the output to the water pressure list
    data.water_pressure_list.append(output)


# TODO reminder: add the vertical pressure on top of the first soil layer after this calculation is done
def calculate_vertical_normal_stress(s_p, data, i):
    """
    Calculates the vertical normal stress.

    :param s_l:
    :param data:
    :return:
    """
    # Output variables
    output = [0, 0]
    # Current soillayer
    s_l = s_p.soil_layer_list[i]
    # Calculate the vertical normal stress for the bottom and top level
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


def calculate_horizontal_normal_stress(s_p, data, i):
    """
    Calculates the horizontal normal stress.

    :param s_l:
    :param data:
    :return:
    """
    # Output variables
    output = [0, 0]
    # Calculate the vertical normal stress for the bottom and top level
    # Top
    output[0] = data.effective_horizontal_normal_stress_list[i][0] + data.water_pressure_list[i][0]
    # Bottom
    output[1] = data.effective_horizontal_normal_stress_list[i][1] + data.water_pressure_list[i][1]
    # Add the output to the horizontal normal stress list
    data.horizontal_normal_stress_list.append(output)


def calculate_effective_vertical_normal_stress(s_p, data, i):
    """
    Calculates the effective vertical normal stress.

    :param s_l:
    :param data:
    :return:
    """
    # Output variables
    output = [0, 0]
    # Calculate the effective vertical normal stress for the bottom and top level
    # Top
    output[0] = data.vertical_normal_stress_list[i][0] - data.water_pressure_list[i][0]
    # Bottom
    output[1] = data.vertical_normal_stress_list[i][1] - data.water_pressure_list[i][1]
    # Add the output to the effective vertical normal stress list
    data.effective_vertical_normal_stress_list.append(output)


def calculate_effective_horizontal_stress(s_p, data, i):
    """
    Calculates teh effective horizontal normal stress.

    :param s_l:
    :param data:
    :param i:
    :return:
    """
    # Output variables
    output = [0, 0]
    # Calculate the effective horizontal normal stress for the bottom and top level
    # Top
    output[0] = s_p.calculate_soil_pressure_coefficient(s_p.soil_layer_list[i].soil.angle) * data.effective_vertical_normal_stress_list[i][0]
    # Bottom
    output[1] = s_p.calculate_soil_pressure_coefficient(s_p.soil_layer_list[i].soil.angle) * data.effective_vertical_normal_stress_list[i][1]
    # Add the output to the effective horizontal normal stress list
    data.effective_horizontal_normal_stress_list.append(output)