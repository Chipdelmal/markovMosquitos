# https://ipython-books.github.io/131-simulating-a-discrete-time-markov-chain/

import network as mntw
import numpy as np

(nNum, mskVct) = (3, [0, .75, .25])
(tol, passMkvTest) = (.99, True)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Define the classes masking matrix
mskMat = mntw.genMskMat(nNum, mskVct)
print(mskMat)
# Check Markovian property
if np.sum(mskMat) < nNum * tol:
    passMkvTest = False
    print("The transitions matrix is not Markovian")
