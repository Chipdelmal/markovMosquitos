# https://ipython-books.github.io/131-simulating-a-discrete-time-markov-chain/

import random
import numpy as np
import seaborn as sns
import aux as aux
import bouts as bts
import network as mntw
import distances as dist
import landscape as land


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# User-Defined
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
random.seed(1)
(classesNum, mskVct) = (3, [.6, .3, .1])
(lo, hi, ptsNum) = (0, 5, 10)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Mosquito biological behaviour
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Create mask matrix: This matrix defines how probable is for a mosquito to
#   move from one life stage to the next (and, as a consequence, from a site
#   type to the next).
mskMat = bts.genMskMat(classesNum, mskVct)
passMkvtest = aux.testMarkovMat(mskMat)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Landscape
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Creates a random landscape (x,y coordinates) and calculates the distances
#   matrix. Also assigns each coordinate a class. It would make sense to have
#   this in a wrapper function to keep coordinates and classes in the same
#   structure.
landscape = land.genURandLandscape(lo, hi, ptsNum)
distMat = dist.distanceMat(landscape)
sns.heatmap(distMat, annot=True)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Migration
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
migrMat = dist.migrationKernel(distMat, .75, 1, 1)
aux.testMarkovMat(migrMat)
sns.heatmap(migrMat, annot=True)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Point types
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
pointClasses = bts.genURandLandscapeClasses(classesNum, ptsNum)
clandMskMat = bts.calcClandMskMat(pointClasses, mskMat)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Full network
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
network = mntw.normalizeMskMgrMat(migrMat, clandMskMat)
aux.testMarkovMat(network)
sns.heatmap(network, annot=True)
