import numpy as np
import math as math


def testMarkovMat(mat, tol):
    if np.sum(mat) < len(mat) * tol:
        return False
    return True


def euclideanDistance(a, b):
    dist = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    return dist


if __name__ == "__main__":
    print(euclideanDistance((0,0), (1, 1)))
