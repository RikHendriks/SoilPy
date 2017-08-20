import pytest
from soilpy import *

def test_water_pressure():
    wl = WaterLayer(0)
    assert wl.water_pressure(-5) == -50
    assert wl.water_pressure(0) == 0
    assert wl.water_pressure(5) == 0
    assert wl.water_pressure(5, True) == 50