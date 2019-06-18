import numpy as np


def testMarkovMat(mat, tol):
    if np.sum(mat) < len(mat) * tol:
        return False
    return True
