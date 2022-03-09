import pytest
import numpy as np
import numerical as nl


class build_wf:
    def __init__(self, myvar, mydim, mydim2=0):
        self.myvar = myvar
        self.mydim = mydim
        self.mydim2 = mydim2

    def init_carray(self):
        arr = np.ones((self.mydim, self.mydim2), dtype=complex)
        return arr * self.myvar

    def init_cvector(self):
        vec = np.ones((self.mydim), dtype=complex)
        return vec * self.myvar

    def init_rarray(self):
        arr = np.ones((self.mydim, self.mydim2), dtype=float)
        return arr * self.myvar


# use markers to pass data to fixtures and then parametrize fixture
@pytest.fixture
def test_wf():
    obj = build_wf(1.0, 3, 3)
    return obj.init_carray()


@pytest.fixture
def test_wf_type():
    obj = build_wf(1.0, 3, 3)
    return obj.init_rarray()


@pytest.fixture
def test_auto():
    obj = build_wf(3.0, 3)
    return obj.init_cvector()


def test_calc_auto(test_wf, test_auto):
    """ Test function to test the calculation of the\
    wave function overlap."""
    # test the computation of values
    assert np.array_equal(nl.calc_auto(test_wf), test_auto)


# test for type errors
def test_calc_auto_type(test_wf_type):
    with pytest.raises(TypeError):
        assert nl.calc_auto(test_wf_type)
