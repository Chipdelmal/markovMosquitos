# https://ipython-books.github.io/131-simulating-a-discrete-time-markov-chain/

import numpy as np
import network as mntw
import aux as aux
import landscape as land

(nNum, mskVct) = (3, [0, .75, .25])
(tol, passMkvTest) = (.99, True)
(lo, hi, ptsNum) = (0, 10, 100)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Mosquito biological behaviour
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Create mask matrix: This matrix defines how probable is for a mosquito to
#   move from one life stage to the next (and, as a consequence, from a site
#   type to the next).
mskMat = mntw.genMskMat(nNum, mskVct)
# aux.testMarkovMat(mskMat, tol)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Landscape
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
landscape = land.genURandLandscape(lo, hi, ptsNum)
distMat = aux.euclideanDistanceMat(landscape)
print(distMat)
