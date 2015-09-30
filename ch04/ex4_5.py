__author__ = 'Indrayana'

import numpy as np

timeLen = 10
maxVal = 10.

# backward dynamic programming
# only for when we still have the asset (otherwise, it will trivially be zero)
optVal = np.zeros(timeLen)
optVal[timeLen-1] = maxVal / 2.

for timeIdx in range(timeLen-1, 0, -1):
    probLower = optVal[timeIdx] / maxVal
    optVal[timeIdx-1] = (1. / (2. * maxVal)  * (maxVal ** 2. - optVal[timeIdx] ** 2.)) + probLower * optVal[timeIdx]

numIter = 1000

values = np.zeros(timeLen)

for iterIdx in range(0, numIter):
    stepSize = 1. / (iterIdx + 1)
    #stepSize = 0.2
    stepSizeComp = 1 - stepSize

    pVec = np.random.rand(timeLen) * maxVal

    for timeIdx in range(0, timeLen):
        reward1 = pVec[timeIdx]
        reward0 = 0
        if timeIdx + 1 < timeLen:
            reward0 = values[timeIdx+1]

        values[timeIdx] = stepSizeComp * values[timeIdx] + stepSize * max(reward0, reward1)