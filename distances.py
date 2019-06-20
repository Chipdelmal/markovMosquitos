import math
import numpy as np
import vincenty as vn


def inverseLinearStep(distance, step, rate, dummy):
    '''
    This function returns a migration estimate based on the inverse of the
        distance. NOTE: This is a terrible way to do it, but it's a first
        approximation. Should be replaced with the zero-inflated exponential.
    '''
    if math.isclose(distance, 0):
        return step
    else:
        return (1 / distance * rate)
    return True


def migrationKernel(distMat, step, rate, dummy):
    coordsNum = len(distMat)
    migrMat = np.empty((coordsNum, coordsNum))
    for (i, row) in enumerate(distMat):
        for (j, dst) in enumerate(row):
            migrMat[i][j] = inverseLinearStep(dst, step, rate, dummy)
        # Normalize rows to sum 1
        migrMat[i] = migrMat[i] / sum(migrMat[i])
    return migrMat


def euclideanDistance(a, b):
    '''
    Should be changed for another function if we are using latlongs.
        Vincenty's formula is available in the pip package.
    '''
    dist = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    return dist


def distanceMat(landscape, distFun=euclideanDistance):
    '''
    Returns the distance matrix according to the provided distance function.
        There's likely a faster implementation using list comprehension, but
        this is readable/good enough for now.
    '''
    coordsNum = len(landscape)
    distMatrix = np.empty((coordsNum, coordsNum))
    for (i, coordA) in enumerate(landscape):
        for (j, coordB) in enumerate(landscape):
            distMatrix[i][j] = distFun(coordA, coordB)
    return distMatrix


if __name__ == "__main__":
    landscape = ((42.3541165, -71.0693514), (40.7791472, -73.9680804))
    distMat = distanceMat(landscape, distFun=vn.vincenty)
    distMat

    row = distMat[0]

    inverseLinearStep(0, .75, 1)
