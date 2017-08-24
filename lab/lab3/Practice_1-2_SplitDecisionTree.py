import numpy as np
from sklearn.datasets import load_iris

def gini(arr):
	classCounts = np.unique(arr, return_counts=True)[1]
	sampleNum = arr.shape[0]
	p_arr = classCounts / float(sampleNum)
	# implement GINI index
	#ret = ???
	ret = 1. - (p_arr**2).sum() 		# expressing gini index formula : 1 - sigma((p_j)^2)
	return ret


def giniSplit(arr1, arr2):
	sampleNum1 = float(arr1.shape[0])
	sampleNum2 = float(arr2.shape[0])
	totalSampleNum = sampleNum1 + sampleNum2
	return gini(arr1) * sampleNum1 / totalSampleNum + \
		   gini(arr2) * sampleNum2 / totalSampleNum

iris = load_iris()           # data load
feature = iris.data          # save the data

minGiniSplit = np.inf        # minimum gini index, these 3 below are variables to be needed for the for-states below
minSplitFeature = None
minSplitBoundary = None

# to calculate which feature has minimum gini index
for fIdx in range(feature.shape[1]):   # repeat four features, because feature.shape[1] = 4,
	featureArr = feature[:,fIdx]       # every row in the fIdx-th column in the data
	uniqueSorted = np.unique(np.sort(featureArr))      # sort and erase the redundant value in featureArr
													   # because what matters now is making the split boundary
													   # we do not need redundant values because it doesn't affect the split boundary,
													   # just making redundant operations

	# to calculate every minimum gini index by splitting every value in featureArr
	# but we have continuous values so first we need to discretize the continuous values
	# so that we'll discretize by spliting every sorted values with a split boundary
	for i in range(len(uniqueSorted)-1):							# for example if we have 4 values then we'll have 3 split boundaries
		splitBoundary = (uniqueSorted[i] + uniqueSorted[i+1]) / 2.  # split the i-th value and the i+1-th value by computing their average
		split1 = iris.target[featureArr <= splitBoundary]           # the values less than splitBoundary would be in split1
		split2 = iris.target[featureArr > splitBoundary]
		giniSplitValue = giniSplit(split1, split2)					# calculate the gini index

		#print fIdx, i, giniSplitValue

		if giniSplitValue < minGiniSplit:                           # find the feature, which has minimum gini index, by comparing the gini index of all the features
			minGiniSplit = giniSplitValue
			minSplitFeature = fIdx
			minSplitBoundary = splitBoundary


print 'minSplitValue:     {}'.format(minGiniSplit)
print 'minSplitFeature:   {}'.format(iris.feature_names[minSplitFeature])  # which feature has minimum gini index?
print 'minSplitBoundary:  {}'.format(minSplitBoundary)
