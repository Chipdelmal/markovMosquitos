import numpy as np
import math as math
import vincenty as vn


def testMarkovMat(mat):
    '''
    Tests that the matrix behaves according to Markov properties (all
        rows sum to 1).
    '''
    rowMkvSums = list(map(sum, mat))
    check = [math.isclose(i, 1) for i in rowMkvSums]
    if check.count(True) == len(mat):
        return True
    return False


def euclideanDistance(a, b):
    '''
    Should be changed for another function if we are using latlongs.
        Vincenty's formula is available in the pip package.
    '''
    dist = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    return dist


def distanceMat(landscape, distFun=euclideanDistance):
    '''
    Returns the distance matrix according to the provided
    '''
    coordsNum = len(landscape)
    distMatrix = np.empty((coordsNum, coordsNum))
    for (i, coordA) in enumerate(landscape):
        for (j, coordB) in enumerate(landscape):
            distMatrix[i][j] = distFun(coordA, coordB)
    return distMatrix

if __name__ == "__main__":
    # print(euclideanDistance((0,0), (1, 1)))
    # print(testMarkovMat(mat))


    landscape = [[42.3541165, -71.0693514], [40.7791472, -73.9680804]]
    distMat = distanceMat(landscape, distFun = vn.vincenty)
    distMat
    
