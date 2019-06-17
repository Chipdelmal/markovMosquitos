import networkx as nx
import numpy as np
import random as rm
import platform


def genMskMat(ntNum=2, vct=[0, 1], tol = .99):
    '''
    This function creates the masking matrix that defines how probable is for
        mosquitos to transition from one state to the next. This assumes the
        change from one state to the next is uniformly probable (mosquitos
        spend the same amount of time in each phase). For a more complicated
        scenario, the matrix should be manually generated.
    '''
    # Make sure the input vector is Markovian
    if np.sum(vct) < tol:
        print(f"Masking vector is not Markovian {np.sum(vct)}")
        return None
    # Generate the mask matrix if the number of classes is equal to the length
    #   to the masking vector.
    if len(vct) != ntNum:
        print(f'''Number of node types ({ntNum}) should be equal to mask
        vector length ({len(vct)}).''')
        return None
    else:
        mskVct = vct
    # Create the mask matrix
    mskMat = np.empty((ntNum, ntNum))
    for i in range(ntNum):
        mskMat[i] = np.roll(mskVct, i)
    return mskMat


if __name__ == "__main__":
    # n: Nodes
    # nt: Nodes types
    (nNum, mskVct) = (3, [0, .75, 0])
    (tol, passMkvTest) = (.99, True)

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Define the classes masking matrix
    mskMat = genMskMat(nNum, mskVct)
    print(mskMat)

    # Check Markovian property
    if np.sum(mskMat) < tol:
        passMkvTest = False
        print("The mask vector is not Markovian")

    # Create the mask matrix
    mskMat = np.empty((ntNum, ntNum))
    for i in range(ntNum):
        mskMat[i] = np.roll(mskVct, i)
    mskMat


    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Define an adjacency matrix manually
     mat = np.matrix([
            [0.2, 0.6, 0.2],
            [0.1, 0.6, 0.3],
            [0.2, 0.7, 0.1]
        ])

    # Check Markovian property
    if map(np.sum, mat) < tol:
        passMkvTest = False
        print("The transitions matrix is not Markovian")
