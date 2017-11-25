import sys
import os
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.cluster.kmeans import KMeansClusterer

vectorizer = TfidfVectorizer(input='filename',decode_error='ignore',min_df=0.5,max_df = 0.8,sublinear_tf=True,use_idf=True)
directoryName = sys.argv[1]
fileList = []
wordvec = None		# This is the vector of all vectors of all the documents

def getFiles():			# Retrieves all the names of the PDF's under fileList
	global fileList
	for filename in os.listdir(directoryName):
	    if filename.endswith(".txt"):
			pathOfFile = 'TextFiles/' + filename
			fileList.append(pathOfFile)

def tf_idf():		# Performs the TFIDF operation and stores the vector of unit vectors under wordvec
	global wordvec
	wordvec = vectorizer.fit_transform(fileList)	# Returns sparse matrix
	wordvec = wordvec.toarray()		# Converts the sparse matrix generated by above as an array

def printClustersInFormat(dict):
	for i in dict:
		print
		print "Cluster " + str(i+1)
		for itemName in dict[i]:
			itemName = itemName.split('/')
			itemName = itemName[1]
			print "\t" + itemName

def main():
	getFiles()
	tf_idf()
	num_clusters = int(sys.argv[2])
	kclusterer = KMeansClusterer(num_clusters, distance=nltk.cluster.util.cosine_distance, repeats=25)
	assigned_clusters = kclusterer.cluster(wordvec, assign_clusters=True)
	clustersDict = {}
	for i in range( num_clusters ):
		clustersDict[i] = []
	for i in range( len(assigned_clusters) ):
		clustersDict[ assigned_clusters[i] ].append(fileList[i])
	printClustersInFormat(clustersDict)


if __name__ == '__main__':
    main()
