import pytest
from soilpy import *

def test_null_tensor():
    assert (np.matrix([[0, 0], [0, 0]]) == null_tensor()).all()