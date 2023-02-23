import pytest
import numpy as np
import numerical as nl


class build_wf:
    def __init__(self):
        pass

    def init_carray(self, myvar, mydim, mydim2):
        arr = np.ones((mydim, mydim2), dtype=complex)
        return arr * myvar

    def init_cvector(self, myvar, mydim):
        vec = np.ones((mydim), dtype=complex)
        return vec * myvar

    def init_rarray(self, myvar, mydim, mydim2):
        arr = np.ones((mydim, mydim2), dtype=float)
        return arr * myvar


# define global variables
test_wf = None
test_auto = None
test_wfr = None


def setup_module(module):
    global test_wf, test_auto, test_wfr
    print("Calling setup")
    obj = build_wf()
    test_wf = obj.init_carray(1.0, 3, 3)
    test_auto = obj.init_cvector(3.0, 3)
    test_wfr = obj.init_rarray(1.0, 3, 3)


def teardown_module(module):
    print("Calling teardown")
    pass


def test_calc_auto():
    """ Test function to test the calculation of the\
    wave function overlap."""
    # test the computation of values
    assert np.array_equal(nl.calc_auto(test_wf), test_auto)


def test_calc_auto_type():
    with pytest.raises(TypeError):
        assert nl.calc_auto(test_wfr)
