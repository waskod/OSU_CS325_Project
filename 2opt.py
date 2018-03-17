# ====================================================================
# Authors:
# Michael Tucker              tuckemic@oregonstate.edu    ID: 933-194-613
# Philip  Michael Sigillito   sigillip@oregonstate.edu    ID: 932-925-316
# Dominic Wasko               waskod@oregonstate.edu      ID: 932-620-942
# CS325 / Traveling Salesman Project
# Date: 3/16/2018
# Description: Solves the traveling salesman optimization problem
# ====================================================================

# =====================================================================
# Imports
# =====================================================================

import sys
import math
import os
import re
from collections import namedtuple


# =====================================================================
# Objects
# =====================================================================

#Node Struct stores vertices EdgeStruct Stores Edges

#Values : Id Number, X Vertex, Y Vertex
NodeStruct = namedtuple("NodeStruct", "number x y")

#Values: Start Vertex, End Vertex, Weight
EdgeStruct = namedtuple("EdgeStruct", "v1 v2 weight")


# =====================================================================
# Functions
# =====================================================================

#Get Distance Between two nodes rounded to the nearest integer
def getWeight(node1, node2):
    weight = math.hypot(node1.x - node2.x, node1.y - node2.y)
    return int(round(weight))

# Gets the input data from the txt file and creates the NodeList with the 
# city number and x and y coordinates stored in each Node
def getInput(fileName, nodeList):
    thisDirectory = os.path.dirname(os.path.abspath(__file__))
    inputFile = os.path.join(thisDirectory, fileName)
    readTextFile = open(inputFile).read().splitlines()
    for i, val in enumerate(readTextFile):
        val = val.lstrip(' ')
        val = re.sub(' +', ' ', val)
        readTextFile[i] = val.split(' ')
        readTextFile[i] = list(map(int, readTextFile[i]))
    for i, node in enumerate(readTextFile):
        currentNode = NodeStruct(node[0], node[1], node[2])
        nodeList.append(currentNode)
    return nodeList

	
# Saves the algorithm results to a file -- 
# the order of the tour and the total distance
def saveResults(fileName, nodeList, finalWeight):
    tourFile = fileName + ".tour"
    writeFile = open(tourFile, 'a+')
    writeFile.write("%s" % finalWeight)
    writeFile.write("\n")
    for i, node in enumerate(nodeList):
        writeFile.write("%s" % nodeList[i].number)
        writeFile.write("\n")
    writeFile.close()


# Calculates the total tour length of a nodeList
def getTotalTourWeight(nodeList):
    nodeCount = len(nodeList)
    totalTourWeight = 0
    for i in range(0, nodeCount - 1):
        totalTourWeight += getWeight(nodeList[i], nodeList[i + 1])
    totalTourWeight += getWeight(nodeList[nodeCount - 1], nodeList[0])
    return totalTourWeight

	
# Creates a vertex pair to display as an edge e.g. (1, 2)
def createVtxPairFromEStrct(edgeStrct):
    vt1 = edgeStrct.v1.number
    vt2 = edgeStrct.v2.number
    edgeStr = "(" + str(vt1) + ", " + str(vt2) + ")"
    return edgeStr

	
# Prints a NodeList on one line
def printNodeList(nodeList):
    nodeStr = ""
    for node in nodeList:
        nodeStr += str(node.number)
        nodeStr += ", "
    nodeStr2 = nodeStr.rstrip(', ')
    nodeStr2 += "\n"
    print(nodeStr2)
    return nodeStr2

	
# Gets the command line arguments and stores them in variables	
def getArgs():
    global cycleCount, fileName, maxSwaps
    argCount = len(sys.argv)
    if argCount > 4 or argCount < 2:
        print("Invalid argument count. Please follow usage:")
        print("python tsp.py <-cycle count> <file name>")
        print("EX: python tsp.py -3 input.txt")
        exit(1)
    if argCount == 2:
        cycleCount = 3
        fileName = sys.argv[1]
        thisDirectory = os.path.dirname(os.path.abspath(__file__))
        inputFile = os.path.join(thisDirectory, fileName)
        if not os.path.isfile(inputFile):
            print("The file: % could not be found in this directory" % fileName)
            exit(1)
    if argCount == 3:
        cycleCount = sys.argv[1]
        fileName = sys.argv[2]
        thisDirectory = os.path.dirname(os.path.abspath(__file__))
        inputFile = os.path.join(thisDirectory, fileName)
        if not os.path.isfile(inputFile):
            print("The file: "+ fileName +" could not be found in this directory")
            exit(1)
        cycleCount = cycleCount[:0] + cycleCount[1:]
        cycleCount = int(cycleCount)
    if argCount == 4:
        cycleCount = sys.argv[2]
        fileName = sys.argv[3]
	maxSwaps = int( sys.argv[1])
        thisDirectory = os.path.dirname(os.path.abspath(__file__))
        inputFile = os.path.join(thisDirectory, fileName)
        if not os.path.isfile(inputFile):
            print("The file: "+ fileName +" could not be found in this directory")
            exit(1)
        cycleCount = cycleCount[:0] + cycleCount[1:]
        cycleCount = int(cycleCount)

		
# Generates an list of Edges for the entire input starting tour
def generateTourEdgeList(cityList):
    tourEdgeList = []
    lenCList = len(cityList)

    for i in range(0, lenCList - 1):
        idStr = str(cityList[i].number) + "_" + str(cityList[i + 1].number)
        newEdge = EdgeStruct(cityList[i], cityList[i + 1], 0)
        tourEdgeList.append(newEdge)
    lastIdStr = str(cityList[lenCList - 1].number) + "_" + str(cityList[0].number)
    lastEdge = EdgeStruct(cityList[lenCList - 1], cityList[0], 0)
    tourEdgeList.append(lastEdge)

    return tourEdgeList    
    

# optimizePath() runs the 2-Opt algorithm	
# Alters NodeList To a Better Tour
# Does Not Calculate Weight

def optimizePath(maxSwaps, numCycles, origNdList, NodeList, EdgeList):
	
	# Create numSwaps counter and set limit on max number of swaps of
	# Edge pairs
    numSwaps = 0
    if (maxSwaps == 0):
         maxSwaps = 10000000
	
    totalTourWeight = getTotalTourWeight(NodeList)
    print("\nInitial totalTourWeight: ")
    print(totalTourWeight)
    print("")

    print("numCycles: " + str(numCycles))
    print("")
    
    print("\nRunning the algorithm...\n")
    
    compareEdgesCounter = 0
    swapCount = 0

	# Outer while loop to run 2-opt for number of cycles through the entire tour
    while compareEdgesCounter < numCycles:
	
		# Outer for loop to start with an existing edge in EdgeList
        for edge1 in EdgeList:
            edge1Str = createVtxPairFromEStrct(edge1)
			
			# Inner for loop to choose an existing edge2 to pair with edge1
            for edge2 in EdgeList:
			
				# if swap limit has been reached, exit the algorithm.
                if(numSwaps == maxSwaps):
                    print("Done with Swaps.")
                    return

				# print numSwaps
				# print maxSwaps		
			 
				# if edge2 is not adjacent to edge1
                if( not(edge1.v1 == edge2.v1 or edge1.v1 == edge2.v2 or edge1.v2 == edge2.v1 or edge1.v2 == edge2.v2)):

					# Calculate existingTotal weight for pair of existing edge1 + edge2
                    existingWeight1 = getWeight(edge1.v1, edge1.v2)
                    existingWeight2 = getWeight(edge2.v1, edge2.v2)
                    existingTotal = (existingWeight1 + existingWeight2)

					# Get NodeList indices for vertices of existing edges
                    A1Index = NodeList.index(edge1.v1)
                    A2Index = NodeList.index(edge1.v2)
                    B1Index = NodeList.index(edge2.v1)
                    B2Index = NodeList.index(edge2.v2)
					
					# Create sorted array of vertex indices
                    finalList = [A1Index, A2Index, B1Index, B2Index]
                    finalList.sort()

					# Calculate newTotal weight for pair of alternate edges
                    newWeight1 = getWeight(NodeList[finalList[0]], NodeList[finalList[2]])
                    newWeight2 = getWeight(NodeList[finalList[1]], NodeList[finalList[3]])
                    newTotal = (newWeight1 + newWeight2)

                    #if New alternate edges are better (have a lower weight), replace old edges with new ones
                    if(newTotal < existingTotal):
                        numSwaps = numSwaps + 1

                        # Create new edges
                        newEdge1 = EdgeStruct(NodeList[finalList[0]], NodeList[finalList[2]], 0)
                        newEdge2 = EdgeStruct(NodeList[finalList[1]], NodeList[finalList[3]], 0)

                        # Get indexes of edges to replace
                        Edge1Index = EdgeList.index(edge1)
                        Edge2Index = EdgeList.index(edge2)

                        # Set edge1 and edge2 to new values for loop
                        edge1 = newEdge1
                        edge2 = newEdge2

                        # Replace Edges in Edgelist
                        EdgeList[Edge1Index] = newEdge1
                        EdgeList[Edge2Index] = newEdge2

						# Generate Node Order in Array from Tracing EdgeList
                        listofEdges = []
                        newOrderNodes = []
						
                        # Copy edgelist
                        for myEdge in EdgeList:
                            listofEdges.append([myEdge.v1.number, myEdge.v2.number])
                            
                        # Get first Node value
                        newOrderNodes.append(listofEdges[0][0])
                        newOrderNodes.append(listofEdges[0][1])
						
                        searchIndex = 1
                            
                        del listofEdges[0]
                            
                        numberOfNodes = len(NodeList)

						# while array length is less than the number of Nodes in NodeList		
                        while len(newOrderNodes) < numberOfNodes:

                            searchValue = newOrderNodes[searchIndex]
                                
                            myCounter = 0
							
							# Build the array by tracing through the edges following 
							# the order of Nodes in each edge
                            for couple in listofEdges:

                                if(couple[0] == searchValue):
                                    newOrderNodes.append(couple[1])
                                    searchIndex = searchIndex + 1
                                    listofEdges[myCounter] = [-1, -1]
                                    break
                                    
                                elif (couple[1] == searchValue):
                                    newOrderNodes.append(couple[0])
                                    searchIndex = searchIndex + 1
                                    listofEdges[myCounter] = [-1, -1]
                                    break
                                    
                                myCounter = myCounter + 1
						
						# Rebuild the working NodeList in the order established by
						# tracing through the edges
                        replaceCounter = 0
                        for myIndex in newOrderNodes:
                            replaceNode = origNdList[myIndex]
                            NodeList[replaceCounter] = replaceNode
                            replaceCounter = replaceCounter + 1

                        replaceTotalTourWeight = getTotalTourWeight(NodeList)
      
        compareEdgesCounter = compareEdgesCounter + 1


if __name__ == '__main__':

    print("\n***** Main *****\n")
    
    # the getArgs function uses global variables. Make sure you have these two variable declared before you call it
    fileName = ""
    cycleCount = -1
    maxSwaps = 0
    getArgs()
    
    workingNodeList = []
    getInput(fileName, workingNodeList)

    origNodeList = []
    getInput(fileName, origNodeList)
    
    workingEdgeList = generateTourEdgeList(workingNodeList)
    print("workingEdgeList length: ")
    print(len(workingEdgeList))
    
    totalTourWeight = getTotalTourWeight(workingNodeList)
        
    #Call 2-Opt Function
    optimizePath(maxSwaps, cycleCount, origNodeList, workingNodeList, workingEdgeList)
        
    print("\nNumber of cities: " + str(len(workingNodeList)) + "\n")
    
    print("Main: Initial totalTourWeight: ")
    print(totalTourWeight)
    
    finalTotalTourWeight = getTotalTourWeight(workingNodeList)
    print("\nMain: finalTotalTourWeight: ")
    print(finalTotalTourWeight)
    print("\n")        

    print("Input file: " + str(fileName))
    print("Saving Results.")
    saveResults(fileName, workingNodeList, finalTotalTourWeight)
    
    print("\nDONE!\n")
