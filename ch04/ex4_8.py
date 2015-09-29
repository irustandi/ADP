__author__ = 'Indrayana'

import numpy as np

gamma = 0.9
numIter = 200
maxValue = 100
timeLen = 21
numMajorIter = 10

actualVals = np.zeros(timeLen)

for timeIdx in range(0, timeLen):
    if timeIdx == 0:
        actualVals[timeLen - timeIdx - 1] = gamma ** timeIdx * (maxValue / 2)
    else:
        actualVals[timeLen - timeIdx - 1] = gamma ** timeIdx * (maxValue / 2) + actualVals[timeLen - timeIdx]

actualVal = actualVals[0]

valueEsts = np.zeros(numMajorIter)

for majorIterIdx in range(0, numMajorIter):
    values = np.zeros(timeLen)
    valueEst = 0
    for iterIdx in range(0, numIter):
        stepSize = 1.0 / (iterIdx + 1)
        stepSizeComp = 1.0 - stepSize

        # get a sample path
        rVec = np.random.rand(timeLen) * maxValue

        for timeIdx in range(timeLen, 0, -1):
            v = rVec[timeIdx-1]
            if timeIdx < timeLen:
                v += gamma * values[timeIdx]

            values[timeIdx-1] = v

        valueEst = (stepSizeComp) * valueEst + stepSize * values[0]

    valueEsts[majorIterIdx] = valueEst