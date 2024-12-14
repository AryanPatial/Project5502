import sys
import os
import numpy as np
import math

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the function to be tested from the production module
from production.functions import predict_subscribe

# Test function to verify the behavior of predict_subscribe
def test_make_prediction():
    # Given
    watch = -8.1
    duration = 1.4
    ctr = -0.7
    interest = 0
    misses = 0.26
    subscribes = 0.73
    # When
    result = predict_subscribe(watch, duration, ctr, interest)

    # Then
    assert isinstance(result, dict)
    assert isinstance(result['Misses Out'], np.float64)
    assert isinstance(result['Subscribes'], np.float64)
    assert math.isclose(result['Misses Out'], misses, abs_tol=0.01)
    assert math.isclose(result['Subscribes'], subscribes, abs_tol=0.01)