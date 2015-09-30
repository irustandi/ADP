__author__ = 'Indrayana'

import numpy as np
import matplotlib.pyplot as plt

def roundPrice(p, delta):
    return round(p / delta, 0) * delta

def generateSample(p0, timeLen):
    pHatVec = np.random.rand(timeLen) * 20 - 10
    pVec = np.zeros(timeLen)
    pVec[0] = p0

    for timeIdx in range(1, timeLen):
        pPrev = pVec[timeIdx-1]
        pVec[timeIdx] = pPrev + 0.5 * (120 - pPrev) + pHatVec[timeIdx]

    return pVec

numIter = 10000
numSamples = 1000
timeLen = 10
p0 = 100

#delta = 1
#delta = 5
delta = 10

valuesTable = dict()

for iterIdx in range(0, numIter):
    stepSize = 1 / (iterIdx + 1)
    stepSizeComp = 1 - 1 / (iterIdx + 1)

    pVec = generateSample(p0, timeLen)

    for timeIdx in range(0, timeLen):
        priceVal = pVec[timeIdx]
        stateVal = int(roundPrice(priceVal, delta))
        stateCurrKey = (timeIdx, stateVal)

        sellReward = priceVal
        keepReward = 0.0
        if timeIdx < timeLen - 1:
            priceNext = pVec[timeIdx+1]
            stateValNext = int(roundPrice(priceNext, delta))
            stateNextKey = (timeIdx + 1, stateValNext)
            if stateNextKey in valuesTable:
                keepReward = valuesTable[stateNextKey]

        newValue = max(sellReward, keepReward)
        oldValue = 0.0

        if stateCurrKey in valuesTable:
            oldValue = valuesTable[stateCurrKey]

        updateValue = stepSizeComp * oldValue + stepSize * newValue
        valuesTable[stateCurrKey] = updateValue

sellTimes = np.zeros(numSamples)

for sampleIdx in range(0, numSamples):
    sampleCurr = generateSample(p0, timeLen)

    for timeIdx in range(0, timeLen):
        pCurr = sampleCurr[timeIdx]
        stateCurr = int(roundPrice(pCurr, delta))

        if not (timeIdx, stateCurr) in valuesTable:
            continue

        if pCurr > valuesTable[(timeIdx, stateCurr)]:
            sellTimes[sampleIdx] = timeIdx
            break

hist, bins = np.histogram(sellTimes, bins=10, range=(0.0, 10.0))
print(hist)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()