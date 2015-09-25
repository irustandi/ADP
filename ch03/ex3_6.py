__author__ = 'Indrayana'

import numpy as np
import tictoc

Ms = [1, 2, 3, 5, 10]

numIter = 50
gamma = 0.8
#stateValues = np.zeros([1, 2])
#stateValues = np.array([100, 100])
stateValues = np.array([100, 0])

transMat = np.array([[0.7, 0.3], [0.05, 0.95]])
contribMat = np.array([[10.0, 30.0], [20.0, 5.0]])
contribVec = np.sum(transMat * contribMat, axis=1)

for M in Ms:
    values = contribVec
    for iter in range(0, numIter):
        m = 0

        tictoc.tic()
        while m < M:
            values = contribVec + gamma * np.dot(transMat, values)
            m += 1

        tictoc.toc()
        print("%s %s: %s" % (M, iter, values[0]))