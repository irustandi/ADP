__author__ = 'indra'

import numpy as np

numIter = 50
gamma = 0.8
#stateValues = np.zeros([1, 2])
#stateValues = np.array([100, 100])
stateValues = np.array([100, 0])

transMat = np.array([[0.7, 0.3], [0.05, 0.95]])
contribMat = np.array([[10.0, 30.0], [20.0, 5.0]])

valueMat = np.zeros([numIter+1, 2])
valueMat[0,] = stateValues

for iter in range(0, numIter):
    # state 1
    state1_1_val = transMat[0, 0] * (contribMat[0, 0] + gamma * valueMat[iter-1, 0])
    state1_2_val = transMat[0, 1] * (contribMat[0, 1] + gamma * valueMat[iter-1, 1])
    valueMat[iter+1,0] = np.max([state1_1_val, state1_2_val])

    # state 2
    state2_1_val = transMat[1, 0] * (contribMat[1, 0] + gamma * valueMat[iter-1, 0])
    state2_2_val = transMat[1, 1] * (contribMat[1, 1] + gamma * valueMat[iter-1, 1])
    valueMat[iter+1,1] = np.max([state2_1_val, state2_2_val])
