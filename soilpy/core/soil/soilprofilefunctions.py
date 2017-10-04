from soilpy.core.plotter import *


class ProfileList:
    """
    Profile lists.
    """
    def __init__(self):
        self.list = []

    def get_value_list(self, level, level_list):
        """
        Returns the value at level with a given level_list for self.list.
        :param level: The level at which the value needs to be calculated.
        :param level_list: The level list which is also a ProfileList.
        :return: Returns the value at level in self.list.
        """
        for i in range(0, len(level_list.list)):
            if level >= level_list.list[i][1]:
                return self.list[i][0] - (((level_list.list[i][0] - level) / (level_list.list[i][0] - level_list.list[i][1])) * (self.list[i][0] - self.list[i][1]))
        return None

    def get_numpy_array(self):
        """
        Returns a flattened numpy array of a list in the soilprofile.
        :param list: A list from the soilprofile class.
        :return: The flattened numpy array of the list.
        """
        return np.array(self.list).flatten()

    def append(self, item):
        """
        Appends item to self.list.
        :param item: The item that needs to be appended
        """
        self.list.append(item)


class SoilProfileData:
    """
    The soil mechanics self class
    """

    def __init__(self, s_p):
        self.soil_profile = s_p
        self.level = ProfileList()
        self.water_pressure = ProfileList()
        self.vertical_normal_stress = ProfileList()
        self.horizontal_normal_stress = ProfileList()
        self.effective_vertical_normal_stress = ProfileList()
        self.effective_horizontal_normal_stress = ProfileList()
        self.plotter = Plotter(self)

    def __str__(self):
        output = "Level: " + str(self.level.get_numpy_array()) + "\n"
        output += "Water pressure: " + str(self.water_pressure.get_numpy_array()) + "\n"
        output += "Vertical normal stress: " + str(self.vertical_normal_stress.get_numpy_array()) + "\n"
        output += "Horizontal normal stress: " + str(self.horizontal_normal_stress.get_numpy_array()) + "\n"
        output += "Effective vertical normal stress: " + str(self.effective_vertical_normal_stress.get_numpy_array()) + "\n"
        output += "Effective horizontal normal stress: " + str(self.effective_horizontal_normal_stress.get_numpy_array())
        return output

    def plot(self, plot_values=True):
        """
        Plots the soil profile
        """
        self.plotter.plot_level_list(self.water_pressure, plot_values)
        self.plotter.plot_level_list(self.vertical_normal_stress, plot_values)
        self.plotter.plot_level_list(self.effective_vertical_normal_stress, plot_values)

    def process_function(self, func):
        """
        Applies func to each soil layer with a given data structure that is passed along.

        :param func:
        :param data:
        :return:
        """
        for i in range(0, len(self.soil_profile.soil_layer_list)):
            func(i)

    def process_soil_mechanics(self):
        """
        Applies all the soil mechanics functions to the data class.

        :param data:
        :return:
        """
        self.process_function(self.calculate_level)
        self.process_function(self.calculate_water_pressure)
        self.process_function(self.calculate_vertical_normal_stress)
        self.process_function(self.calculate_effective_vertical_normal_stress)
        self.process_function(self.calculate_effective_horizontal_stress)
        self.process_function(self.calculate_horizontal_normal_stress)

    def calculate_level(self, i):
        """
        Calculates the level.

        :param self.soil_profile:
        :param self:
        :param i:
        :return:
        """
        # Output variables
        output = [0, 0]
        # Current soillayer
        s_l = self.soil_profile.soil_layer_list[i]
        # Calculate the level for the bottom and top level
        # Top
        output[0] = s_l.top_level
        # Bottom
        output[1] = s_l.bottom_level
        # Add the output to the water pressure list
        self.level.append(output)

    def calculate_water_pressure(self, i):
        """
        Calculates the water pressure.

        :param s_l:
        :param self:
        :return:
        """
        # Output variables
        output = [0, 0]
        # Current soillayer
        s_l = self.soil_profile.soil_layer_list[i]
        # Calculate the water pressure for the bottom and top level
        # If the water level is above the top level of the soil layer
        if s_l.water_layer.level + s_l.capillary_rise >= s_l.top_level:
            output[0] = s_l.water_layer.gamma * (s_l.water_layer.level - s_l.top_level)
            output[1] = s_l.water_layer.gamma * (s_l.water_layer.level - s_l.bottom_level)
        # Add the output to the water pressure list
        self.water_pressure.append(output)

    # TODO reminder: add the vertical pressure on top of the first soil layer after this calculation is done
    def calculate_vertical_normal_stress(self, i):
        """
        Calculates the vertical normal stress.

        :param s_l:
        :param self:
        :return:
        """
        # Output variables
        output = [0, 0]
        # Current soillayer
        s_l = self.soil_profile.soil_layer_list[i]
        # Calculate the vertical normal stress for the bottom and top level
        # If it is not the first layer
        if i is not 0:
            output[0] = self.vertical_normal_stress.list[i - 1][1]
        # If the soil is saturated or not
        if s_l.water_layer.level + s_l.capillary_rise >= s_l.top_level:
            output[1] = output[0] + s_l.thickness * s_l.soil.gamma_saturated
        else:
            output[1] = output[0] + s_l.thickness * s_l.soil.gamma
        # Add the output to the vertical normal stress list
        self.vertical_normal_stress.append(output)

    def calculate_horizontal_normal_stress(self, i):
        """
        Calculates the horizontal normal stress.

        :param s_l:
        :param self:
        :return:
        """
        # Output variables
        output = [0, 0]
        # Calculate the vertical normal stress for the bottom and top level
        # Top
        output[0] = self.effective_horizontal_normal_stress.list[i][0] + self.water_pressure.list[i][0]
        # Bottom
        output[1] = self.effective_horizontal_normal_stress.list[i][1] + self.water_pressure.list[i][1]
        # Add the output to the horizontal normal stress list
        self.horizontal_normal_stress.append(output)

    def calculate_effective_vertical_normal_stress(self, i):
        """
        Calculates the effective vertical normal stress.

        :param s_l:
        :param self:
        :return:
        """
        # Output variables
        output = [0, 0]
        # Calculate the effective vertical normal stress for the bottom and top level
        # Top
        output[0] = self.vertical_normal_stress.list[i][0] - self.water_pressure.list[i][0]
        # Bottom
        output[1] = self.vertical_normal_stress.list[i][1] - self.water_pressure.list[i][1]
        # Add the output to the effective vertical normal stress list
        self.effective_vertical_normal_stress.append(output)

    def calculate_effective_horizontal_stress(self, i):
        """
        Calculates teh effective horizontal normal stress.

        :param s_l:
        :param self:
        :param i:
        :return:
        """
        # Output variables
        output = [0, 0]
        # Calculate the effective horizontal normal stress for the bottom and top level
        # Top
        output[0] = self.soil_profile.calculate_soil_pressure_coefficient(self.soil_profile.soil_layer_list[i].soil.angle) * self.effective_vertical_normal_stress.list[i][0]
        # Bottom
        output[1] = self.soil_profile.calculate_soil_pressure_coefficient(self.soil_profile.soil_layer_list[i].soil.angle) * self.effective_vertical_normal_stress.list[i][1]
        # Add the output to the effective horizontal normal stress list
        self.effective_horizontal_normal_stress.append(output)