# https://ipython-books.github.io/131-simulating-a-discrete-time-markov-chain/

import numpy as np
import network as mntw
import aux as aux

(nNum, mskVct) = (3, [0, .75, .25])
(tol, passMkvTest) = (.99, True)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Define the masking matrix
#   This matrix defines how probable is for a mosquito to move from one life
#   stage to the next (and, as a consequence, from a site type to the next).
mskMat = mntw.genMskMat(nNum, mskVct)
aux.testMarkovMat(mskMat, tol)
