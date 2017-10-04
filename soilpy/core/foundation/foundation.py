from soilpy.core.soil import *
import math


# TODO make a process class that is more abstract then SoilMechanics and inherit that class and have SoilMechanics as a single input
class SinglePile(SoilMechanics):
    """
    Single pile foundation
    """
    def __init__(self, s_p, ):
        # Initialize the Soil Mechanics subclass
        super(SinglePile, self).__init__(s_p)
        # Initialize all the new variables
        self.negative_stick = 0

    def __str__(self):
        output = super(SinglePile, self).__str__() + "\n"
        output += "Negative stick: " + str(self.negative_stick)
        return output

    # TODO the name 'negative stick' needs to be changed to the proper name
    def calculate_negative_stick(self, perimeter, made_in_soil=False):
        """

        :param i:
        :return:
        """
        # Output variables
        output = 0

        # Calculate the negative stick for each layer
        for i in range(0, len(self.soil_profile.soil_layer_list)):
            angle = self.soil_profile.soil_layer_list[i].soil.angle
            k0 = 1 - math.sin(math.radians(angle))
            if not made_in_soil:
                angle *= 0.75

            c = k0 * math.tan(math.radians(angle))
            if c < 0.25:
                c = 0.25

            output += self.soil_profile.soil_layer_list[i].thickness * c * ((self.effective_vertical_normal_stress.list[i][0] + self.effective_vertical_normal_stress.list[i][1]) / 2)

        # Add the output to the water pressure list
        self.negative_stick = perimeter * output


class GroupPile(SoilMechanics):
    """
    Group pile foundation
    """
    def __init__(self, s_p, ):
        # Initialize the Soil Mechanics subclass
        super(GroupPile, self).__init__(s_p)
        # Initialize all the new variables
        self.negative_stick = 0

    def __str__(self):
        output = super(GroupPile, self).__str__() + "\n"
        output += "Negative stick: " + str(self.negative_stick)
        return output

    # TODO the name 'negative stick' needs to be changed to the proper name
    def calculate_negative_stick(self, area, perimeter, made_in_soil=False):
        """

        :param i:
        :return:
        """
        # Output variables
        output = [0]

        # Calculate the negative stick for each layer
        for i in range(0, len(self.soil_profile.soil_layer_list)):
            angle = self.soil_profile.soil_layer_list[i].soil.angle
            k0 = 1 - math.sin(math.radians(angle))
            if not made_in_soil:
                angle *= 0.75

            c = k0 * math.tan(math.radians(angle))
            if c < 0.25:
                c = 0.25

            # The following needs to be changed
            m = (perimeter / area) * c

            output += self.soil_profile.soil_layer_list[i].thickness * c * ((self.effective_vertical_normal_stress.list[i][0] + self.effective_vertical_normal_stress.list[i][1]) / 2)

        # Add the output to the water pressure list
        self.negative_stick = perimeter * output