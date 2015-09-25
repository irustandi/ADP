__author__ = 'indra'

import numpy as np
import matplotlib.pyplot as plt

numIter = 50
gamma = 0.8
#stateValues = np.zeros([1, 2])
#stateValues = np.array([100, 100])
stateValues = np.array([100, 0])

transMat = np.array([[0.7, 0.3], [0.05, 0.95]])
contribMat = np.array([[10.0, 30.0], [20.0, 5.0]])
contribVec = np.sum(transMat * contribMat, axis=1)

valueMat = np.zeros([numIter+1, 2])
valueMat[0,] = stateValues

for iter in range(0, numIter):
    # state 1
    valueMat[iter+1,0] = contribVec[0] + gamma * (transMat[0,0] * valueMat[iter,0] + transMat[0,1] * valueMat[iter,1])

    # state 2
    valueMat[iter+1,1] = contribVec[1] + gamma * (transMat[1,0] * valueMat[iter,0] + transMat[1,1] * valueMat[iter,1])

plt.plot(valueMat[:,0])
plt.show()