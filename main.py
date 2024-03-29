# https://ipython-books.github.io/131-simulating-a-discrete-time-markov-chain/

import random
import seaborn as sns
import aux as aux
import bouts as bts
import network as mntw
import landscape as land
import MoNeT_MGDrivE as monet

# ########################################################################
# User-Defined
# ########################################################################
random.seed(1)
(classesNum, mskVct, zeroInflation) = (1, [1], .75)
(lo, hi, ptsNum) = (0, 10, 3)

# ########################################################################
# Mosquito biological behaviour
# ########################################################################
# Create mask matrix: This matrix defines how probable is for a mosquito to
#   move from one life stage to the next (and, as a consequence, from a site
#   type to the next).
mskMat = bts.genMskMat(classesNum, mskVct)
passMkvtest = aux.testMarkovMat(mskMat)

# ########################################################################
# Landscape
# ########################################################################
# Creates a random landscape (x,y coordinates) and calculates the distances
#   matrix. Also assigns each coordinate a class. It would make sense to have
#   this in a wrapper function to keep coordinates and classes in the same
#   structure.
landscape = land.genURandLandscape(lo, hi, ptsNum)
distMat = monet.calculateDistanceMatrix(landscape)
sns.heatmap(distMat, annot=True)

# ########################################################################
# Migration
# ########################################################################
migrMat = monet.zeroInflatedExponentialMigrationKernel(
    distMat,
    params=monet.AEDES_EXP_PARAMS,
    zeroInflation=.75
)
aux.testMarkovMat(migrMat)
sns.heatmap(migrMat, annot=True)

# ########################################################################
# Point types
# ########################################################################
pointClasses = bts.genURandLandscapeClasses(classesNum, ptsNum)
clandMskMat = bts.calcClandMskMat(pointClasses, mskMat)

# ########################################################################
# Full network
# ########################################################################
network = mntw.normalizeMskMgrMat(migrMat, clandMskMat)
aux.testMarkovMat(network)
sns.heatmap(network, annot=True)
