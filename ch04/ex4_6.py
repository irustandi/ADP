__author__ = 'Indrayana'

import numpy as np
import matplotlib.pyplot as plt

def roundPrice(p, delta):
    return round(p / delta, 0) * delta

def getNextSample(p):
    randNum = np.random.rand() * 20 - 10
    pNext = p + 0.5 * (120 - p) + randNum

    return pNext

def generateSample(p0, timeLen):
    pVec = np.zeros(timeLen)
    pVec[0] = p0

    for timeIdx in range(1, timeLen):
        pPrev = pVec[timeIdx-1]
        pVec[timeIdx] = getNextSample(pPrev)

    return pVec

numIter = 10000
numSamples = 1000
numSamplesInner = 100
timeLen = 10
p0 = 100

#delta = 1
delta = 5
#delta = 10

valuesTable = dict()

# first try
# for iterIdx in range(0, numIter):
#     stepSize = 1 / (iterIdx + 1)
#     stepSizeComp = 1 - 1 / (iterIdx + 1)
#
#     pVec = generateSample(p0, timeLen)
#
#     for timeIdx in range(0, timeLen):
#         priceVal = pVec[timeIdx]
#         stateVal = int(roundPrice(priceVal, delta))
#         stateCurrKey = (timeIdx, stateVal)
#
#         sellReward = priceVal
#         keepReward = 0.0
#         if timeIdx < timeLen - 1:
#             priceNext = pVec[timeIdx+1]
#             stateValNext = int(roundPrice(priceNext, delta))
#             stateNextKey = (timeIdx + 1, stateValNext)
#             if stateNextKey in valuesTable:
#                 keepReward = valuesTable[stateNextKey]
#
#         newValue = max(sellReward, keepReward)
#         oldValue = 0.0
#
#         if stateCurrKey in valuesTable:
#             oldValue = valuesTable[stateCurrKey]
#
#         updateValue = stepSizeComp * oldValue + stepSize * newValue
#         valuesTable[stateCurrKey] = updateValue

# based on Fig 4.2 of 1st ed
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

        # samples
        for sampleIdx in range(0, numSamplesInner):
            priceNextSample = getNextSample(priceVal)
            stateNextSample = int(roundPrice(priceNextSample, delta))
            stateNextKey = (timeIdx + 1, stateNextSample)

            if stateNextKey in valuesTable:
                keepReward += 1 / numSamples * valuesTable[stateNextKey]

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
        if timeIdx + 1 == timeLen:
            sellTimes[sampleIdx] = timeIdx
            break

        pCurr = sampleCurr[timeIdx]
        pNext = sampleCurr[timeIdx+1]
        stateCurr = int(roundPrice(pCurr, delta))
        stateNext = int(roundPrice(pNext, delta))

        #if not (timeIdx + 1, stateNext) in valuesTable or pCurr > valuesTable[(timeIdx + 1, stateNext)]:
        if not(timeIdx, stateCurr) in valuesTable or pCurr > valuesTable[(timeIdx, stateCurr)]:
            sellTimes[sampleIdx] = timeIdx
            break

print(valuesTable)
hist, bins = np.histogram(sellTimes, bins=10, range=(0.0, 10.0))
print(hist)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()