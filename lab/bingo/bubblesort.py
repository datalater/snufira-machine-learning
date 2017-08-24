import sys
import numpy as np

counter=0
def bubbleSort(alist):
	global counter
	for passnum in range(len(alist)-1,0,-1):

		for i in range(passnum):
			#print "Iteration %s:\t%s"%(counter, alist)
			if alist[i]>alist[i+1]:
				print "check if i is larger than i+1, and if so, swap i and i+1"				

			counter+=1

def main():

	myList=[57, 100, 96, 93, 8, 78, 40, 3, 99, 23, 59, 83, 22, 74, 10, 58, 19, 17, 91, 35]

	#### EVALUATION PART START ####
	#
	#data_n=int(sys.argv[1])	
	#myList = np.random.random_integers(0, 10000, data_n).tolist()
	#print "bubblesort", data_n, counter
	#### EVALUATION PART END ####

	bubbleSort(myList)
	print "Result:\t%s"%(myList)
#	print counter


if __name__=="__main__":
	main()
