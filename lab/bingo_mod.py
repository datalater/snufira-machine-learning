import random

def initMatrix(n) :
	randomInts = range(1, n*n+1)	# generate random number
	random.shuffle(randomInts)		# shufflel random numbers

	# task: create a n by n matrix and fill it with the random numbers
	mat = []
	for i in range(n) :
		# 1 line code
		mat.append([])
		for j in range(n) :
			# 1 line code
			mat[i].append(randomInts[i*n+j])

	return mat

def updateMatrix(mat, bn):
	# loop through i
	for idx, i in enumerate(mat):
		print idx, i

		# loop through j
		#for ... :
			# task: check if j=bn and mark the cell with "*" (1 line code)
		if bn in i:
			for j in range(len(i)):
				if bn == i[j]:
					i[j] = "*"

def printMatrix(mat) :
	for l in mat :
		print '\t'.join(map(str, l))
