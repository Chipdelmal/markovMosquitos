import numpy as np
import math as math


def testMarkovMat(mat, tol):
    '''
    Tests that the matrix behaves according to Markov properties (all)
        rows sum to 1 (this is not a thorough test and has a major flaw
        but works for now).
    '''
    vct = map(sum, mat)
    print(f"{sum(vct)} , {len(mat) * tol} = {sum(vct) >= (len(mat) * tol)}")
    if sum(map(float, vct)) >= float((len(mat) * tol)):
        return True
    return False


def euclideanDistance(a, b):
    '''
    Should be changed for another function if we are using latlongs.
    '''
    dist = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    return dist


def euclideanDistanceMat(landscape, distFun=euclideanDistance):
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
    #print(euclideanDistance((0,0), (1, 1)))
    tol=.99
    mat = [[0,.5,.5],[0,.5,.5],[1,0,0]]
    vct = map(sum, mat)
    sum(list(vct))
    type(len(mat) * tol)
    sum(vct) > (len(mat) * tol)

    sum([i >= tol for i in vct])
    print(testMarkovMat(mat,.95))

    float(sum(vct)) >= float((len(mat) * tol))
