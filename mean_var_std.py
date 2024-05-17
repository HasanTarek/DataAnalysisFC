
import random
import numpy as np

try:

    inputArray = []

    for x in range(1, 10):
      inputArray.append(random.randint(1, 10))
    length = len(inputArray)
    
    if length != 9:
        raise Exception("List must contain nine numbers.")

    numpyArray = np.array(inputArray)
    numpyMatrix = numpyArray.reshape(3, 3)

    axis1 = np.mean(numpyMatrix, axis=0).tolist()
    axis2 = np.mean(numpyMatrix, axis=1).tolist()
    flattened = np.mean(numpyMatrix)

    variance1 = np.var(numpyMatrix, axis=0).tolist()
    variance2 = np.var(numpyMatrix, axis=1).tolist()
    variance3 = np.var(numpyMatrix)

    standardDev1 = np.std(numpyMatrix, axis=0).tolist()
    standardDev2 = np.std(numpyMatrix, axis=1).tolist()
    standardDev3 = np.std(numpyMatrix)

    max1 = np.max(numpyMatrix, axis=0).tolist()
    max2 = np.max(numpyMatrix, axis=1).tolist()
    maxFlat = np.max(numpyMatrix)

    min1 = np.min(numpyMatrix, axis=0).tolist()
    min2 = np.min(numpyMatrix, axis=1).tolist()
    minFlat = np.min(numpyMatrix)

    sum1 = np.sum(numpyMatrix, axis=0).tolist()
    sum2 = np.sum(numpyMatrix, axis=1).tolist()
    sumFlat = np.sum(numpyMatrix)

    thisdict = {
        "mean": [axis1, axis2, flattened],
        "variance": [variance1, variance2, variance3],
        "standard deviation": [standardDev1, standardDev2, standardDev3],
        "max": [max1, max2, maxFlat],
        "min": [min1, min2, minFlat],
        "sum": [sum1, sum2, sumFlat]
    }

    print(thisdict)

except ValueError as errMsg:
    print(errMsg)
