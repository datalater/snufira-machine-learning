import sys
import numpy as np

counter=0	# counter index

# quick sort
def partition(myList, start, end):
	global counter

	pivot = myList[start]
	left = start+1
	# Start outside the area to be partitioned
	right = end
	done = False

	while not done:
		while left <= right and myList[left] <= pivot:
			left = left + 1
		while myList[right] >= pivot and right >=left:
			right = right -1
		if right < left:
			done= True
		else:
			# swap places
			temp=myList[left]
			myList[left]=myList[right]
			myList[right]=temp

		counter+=1
		#print "Iteration %d (%d): %s"%(counter, pivot, myList)


	# swap start with myList[right]
	temp=myList[start]
	myList[start]=myList[right]
	myList[right]=temp
	return right


def quicksort(myList, start, end):
	if start < end:
		# partition the list
		split = partition(myList, start, end)

		# sort both halves
		quicksort(myList, start, split-1)
		quicksort(myList, split+1, end)
	return myList


def main():


	myList=[57, 100, 96, 93, 8, 78, 40, 3, 99, 23, 59, 83, 22, 74, 10, 58, 19, 17, 91, 35]	# 20 data
	data_n=len(myList)

	#### EVALUATION PART START ####
	#
	#data_n=int(sys.argv[1])	
	#myList = np.random.random_integers(0, 10000, data_n).tolist()
	#print "quicksort", data_n, counter
	#
	#### EVALUATION PART END ####

	sortedList = quicksort(myList,0,len(myList)-1)
	print "Result: %s"%(sortedList)
	#print counter


if __name__=="__main__":
	main()
