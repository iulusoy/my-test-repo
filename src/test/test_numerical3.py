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


@pytest.fixture(scope="module")
def init_obj():
    # print('Calling setup')
    obj = build_wf()
    return obj
    # if you want to use a teardown method:
    # yield obj
    # print('Cleaning up')


@pytest.fixture()
def get_wf(init_obj):
    test_wf = init_obj.init_carray(1.0, 3, 3)
    test_auto = init_obj.init_cvector(3.0, 3)
    return test_wf, test_auto


@pytest.fixture()
def get_wfr(init_obj):
    return init_obj.init_rarray(1.0, 3, 3)


def test_calc_auto(get_wf):
    """ Test function to test the calculation of the\
    wave function overlap."""
    # test the computation of values
    assert np.array_equal(nl.calc_auto(get_wf[0]), get_wf[1])


# test for type errors
def test_calc_auto_type(get_wfr):
    with pytest.raises(TypeError):
        assert nl.calc_auto(get_wfr)
