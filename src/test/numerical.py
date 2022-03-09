import numpy as np


def aucofu(wavef):
    """Function to compute the autocorrelation function from the
    given vectors (with respect to the first time step).

    Args:
        wavef (numpy array, complex): The wave function\
        over time.

    Returns:
        numpy array, complex: The autocorrelation\
        function over time.

    """
    # store the time column in a vector and drop from array
    time = wavef[0]
    wavef = np.delete(wavef, [0], axis=0)
    # convert to complex array
    realpart = wavef[0::2]
    imagpart = wavef[1::2]
    wavefc = realpart + 1j * imagpart
    # Now construct overlap between first vector and all others
    aucofu = calc_auto(wavefc)
    return time, aucofu


def calc_auto(wavef):
    """Helper function to compute the vector overlap.

    Args:
        wavef (numpy array, complex): The wave function over time.

    Returns:
        numpy array, complex: The autocorrelation function over time."""
    aucofu = np.zeros(len(wavef[0]), dtype=complex)
    if type(wavef.item(0)) != complex:
        print("Found ", type(wavef.item(0)))
        raise TypeError("calc auto received wrong type of wavefunction data!")
    for i in range(0, len(wavef[0])):
        aucofu[i] = np.sum(np.conjugate(wavef[:, 0]) * wavef[:, i])
    return aucofu
