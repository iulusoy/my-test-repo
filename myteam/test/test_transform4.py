import pytest
import numpy as np
import transform as tf


@pytest.fixture()
def return_circle_vals(request):
    marker = request.node.get_closest_marker("setval")
    if marker == "None":
        # missing marker
        print("Missing a marker for circle values")
    else:
        r_val = marker.args[0]
        A_val = marker.args[1]
        # put in get_vals only to demonstrate how to access kwargs
        get_vals = marker.kwargs.get("get")
        if get_vals:
            print("Yes!")
    return r_val, A_val


@pytest.mark.setval(1, np.pi, get=False)
def test_area_circ(return_circle_vals):
    """Test the area values against a reference for r >= 0."""
    myinput, myref = return_circle_vals
    assert tf.area_circ(myinput) == myref
