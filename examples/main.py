from soilpy import *

water_level = WaterLayer(1)

sand = Soil(18, 20, 30)
clay = Soil(17, 17, 35)

s_p = SoilProfile("n")
s_p.add_soil_layer(SoilLayer(sand, water_level, 0, -2))
s_p.add_soil_layer(SoilLayer(clay, water_level, -2, -4))
s_p.add_soil_layer(SoilLayer(sand, water_level, -4, -10))

data = SoilProfileData()

s_p.process_soil_mechanics(data)

print(data)
