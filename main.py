# https://ipython-books.github.io/131-simulating-a-discrete-time-markov-chain/

import numpy as np
import network as mntw
import aux as aux
import landscape as land

(classNum, mskVct) = (3, [0, .75, .25])
(lo, hi, ptsNum) = (0, 10, 10)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Mosquito biological behaviour
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Create mask matrix: This matrix defines how probable is for a mosquito to
#   move from one life stage to the next (and, as a consequence, from a site
#   type to the next).
mskMat = mntw.genMskMat(classNum, mskVct)
passMkvtest = aux.testMarkovMat(mskMat)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Landscape
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Creates a random landscape (x,y coordinates) and calculates the distances
#   matrix. Also assigns each coordinate a class. It would make sense to have
#   this in a wrapper function to keep coordinates and classes in the same
#   structure. 
landscape = land.genURandLandscape(lo, hi, ptsNum)
distMat = aux.distanceMat(landscape)
pointClasses = land.genURandLandscapeClasses(classNum, ptsNum)

print(pointClasses)
