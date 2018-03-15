# ====================================================================
# Authors:
# Michael Tucker              tuckemic@oregonstate.edu    ID: 933-194-613
# Philip  Michael Sigillito   sigillip@oregonstate.edu    ID:
# Dominic Wasko               waskod@oregonstate.edu      ID: 932-620-942
# CS325 / Traveling Salesman Project
# Date: 3/13/2018
# Description: solves the traveling salesman optimization problem
# ====================================================================

# =====================================================================
# Imports
# =====================================================================

import sys
import math
import os
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


def getInput(fileName, nodeList):
    thisDirectory = os.path.dirname(os.path.abspath(__file__))
    inputFile = os.path.join(thisDirectory, fileName)
    readTextFile = open(inputFile).read().splitlines()
    for i, val in enumerate(readTextFile):
        readTextFile[i] = readTextFile[i].split(' ')
        readTextFile[i] = list(map(int, readTextFile[i]))
    for i, node in enumerate(readTextFile):
        currentNode = NodeStruct(node[0], node[1], node[2])
        nodeList.append(currentNode)
    return nodeList


def getTotalTourWeight(nodeList):
    nodeCount = len(nodeList)
    totalTourWeight = 0
    for i in range(0, nodeCount - 1):
        totalTourWeight += getWeight(nodeList[i], nodeList[i + 1])
    totalTourWeight += getWeight(nodeList[nodeCount - 1], nodeList[0])
    return totalTourWeight


def createVtxPairFromEStrct(edgeStrct):
    vt1 = edgeStrct.v1.number
    vt2 = edgeStrct.v2.number
    edgeStr = "(" + str(vt1) + ", " + str(vt2) + ")"
    return edgeStr


def printNodeList(nodeList):
    nodeStr = ""
    for node in nodeList:
        nodeStr += str(node.number)
        nodeStr += ", "
    nodeStr2 = nodeStr.rstrip(', ')
    nodeStr2 += "\n"
    print(nodeStr2)
    return nodeStr2


# Currently broken due to EdgeStruct incompatibilty
# def changeEdgeInfo(edgeStrct, newEndNodeNum):
    # EdgeStruct = namedtuple("EdgeStruct", "v1 v2 weight")
#    startNodeNum = edgeStrct.v1.number
#    newIdStr = str(startNodeNum) + "_" + str(newEndNodeNum)
#    edgeStrct = edgeStrct._replace(v2.number = newEndNodeNum)
    # edgeStrct = edgeStrct._replace(id = newIdStr, endNode = newEndNodeNum)
#    return edgeStrct


def generateTourEdgeList(cityList):
    tourEdgeList = []
    lenCList = len(cityList)

    for i in range(0, lenCList - 1):
        idStr = str(cityList[i].number) + "_" + str(cityList[i + 1].number)
        # EdgeStruct = namedtuple("EdgeStruct", "v1 v2 weight")
        newEdge = EdgeStruct(cityList[i], cityList[i + 1], 0)
        # newEdge = EdgeStruct(idStr, cityList[i].number, cityList[i + 1].number, 0)
        tourEdgeList.append(newEdge)

    # Add the last edge connecting last node to origin node
    lastIdStr = str(cityList[lenCList - 1].number) + "_" + str(cityList[0].number)
    lastEdge = EdgeStruct(cityList[lenCList - 1], cityList[0], 0)
    # lastEdge = EdgeStruct(lastIdStr, cityList[lenCList - 1].number, cityList[0].number, 0)
    tourEdgeList.append(lastEdge)

    return tourEdgeList    
    



#*********************
#TEST DATA
#*********************

#Test Nodes
# A = NodeStruct(0, 485, 6238)
# B = NodeStruct(1, 11, 2579)
# C = NodeStruct(2, 1651, 4220)
# D = NodeStruct(3, 74, 1493)
# E = NodeStruct(4, 1, 1)
# F = NodeStruct(5, 1959, 33)
# G = NodeStruct(6, 1, 56)
# H = NodeStruct(7, 4659, 563)

# A = NodeStruct(0, 200, 800)
# B = NodeStruct(1, 3600, 2300)
# C = NodeStruct(2, 3100, 3300)
# D = NodeStruct(3, 4700, 5750)
# E = NodeStruct(4, 5400, 5750)
# F = NodeStruct(5, 5608, 7103)
# G = NodeStruct(6, 4493, 7102)
# H = NodeStruct(7, 3600, 6950)

#Test Edges
# eA = EdgeStruct(A, B, 0)
# eB = EdgeStruct(B, C, 0)
# eC = EdgeStruct(C, D, 0)
# eD = EdgeStruct(D, E, 0)
# eE = EdgeStruct(E, A, 0)  # for set of 5 nodes case
# eE = EdgeStruct(E, F, 0)
# eF = EdgeStruct(F, G, 0)
# eG = EdgeStruct(G, H, 0)
# eH = EdgeStruct(H, A, 0)

#*********************
#End Test Data
#*********************

#List of Nodes and Edges Must Be in same order received From File
#NodeList Represents the Tour
# origNodeList = [A, B, C, D, E, F, G, H]
# NodeList = [A, B, C, D, E, F, G, H]
# NodeCount = len(NodeList)

# totalTourWeight = getTotalTourWeight(NodeList)
# print("Initial totalTourWeight: ")
# print(totalTourWeight)
# print("\n")

# print("\nInitial NodeList")
# initialNodeListStr = printNodeList(NodeList)

# EdgeList = [eA, eB, eC, eD, eE, eF, eG, eH]
# EdgeCount = len(EdgeList)



#Alters NodeList To a Better Tour
#Does Not Calculate Weight
#Need to Modularize Parts into seperate functions

def optimizePath(origNdList, NodeList, EdgeList):

    totalTourWeight = getTotalTourWeight(NodeList)
    print("Initial totalTourWeight: ")
    print(totalTourWeight)
    print("\n")

    numCycles = 3
    compareEdgesCounter = 0
    swapCount = 0

    while compareEdgesCounter < numCycles:
        for edge1 in EdgeList:
            edge1Str = createVtxPairFromEStrct(edge1)
            for edge2 in EdgeList:
                if( not(edge1.v1 == edge2.v1 or edge1.v1 == edge2.v2 or edge1.v2 == edge2.v1 or edge1.v2 == edge2.v2)):

                    existingWeight1 = getWeight(edge1.v1, edge1.v2)
                    existingWeight2 = getWeight(edge2.v1, edge2.v2)
                    existingTotal = (existingWeight1 + existingWeight2)

                    A1Index = NodeList.index(edge1.v1)
                    A2Index = NodeList.index(edge1.v2)

                    B1Index = NodeList.index(edge2.v1)
                    B2Index = NodeList.index(edge2.v2)

                    finalList = [A1Index, A2Index, B1Index, B2Index]
                    finalList.sort()

                    newWeight1 = getWeight(NodeList[finalList[0]], NodeList[finalList[2]])
                    newWeight2 = getWeight(NodeList[finalList[1]], NodeList[finalList[3]])
                    newTotal = (newWeight1 + newWeight2)

                    #if New edges are better, replace old edges
                    if(newTotal < existingTotal):

                        print("\n              REPLACE!\n")
                        
                        swapCount += 1

                        #create new edges
                        newEdge1 = EdgeStruct(NodeList[finalList[0]], NodeList[finalList[2]], 0)
                        newEdge2 = EdgeStruct(NodeList[finalList[1]], NodeList[finalList[3]], 0)

                        #get indexes of edges to replace
                        Edge1Index = EdgeList.index(edge1)
                        Edge2Index = EdgeList.index(edge2)

                        #set edge1 and edge2 to new values for loop
                        edge1 = newEdge1
                        edge2 = newEdge2

                        #Replace Edges in Edgelist
                        EdgeList[Edge1Index] = newEdge1
                        EdgeList[Edge2Index] = newEdge2

                        #copy edgelist
                        listofEdges = []
                        newOrderNodes = []
                        
                        for myEdge in EdgeList:
                            listofEdges.append([myEdge.v1.number, myEdge.v2.number])
                            
                        #get first value
                        newOrderNodes.append(listofEdges[0][0])
                        newOrderNodes.append(listofEdges[0][1])
                        searchIndex = 1
                        # print(newOrderNodes)
                            
                        del listofEdges[0]
                            
                        numberOfNodes = len(NodeList)

                        while len(newOrderNodes) < numberOfNodes:

                            searchValue = newOrderNodes[searchIndex]
                                
                            myCounter = 0
                                
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

                            # print("New Order Nodes and List of Edges")
                            # print(newOrderNodes)
                            # print(listofEdges)

                        # print("Nodes Going In")
                        # print(newOrderNodes)

                        replaceCounter = 0
                        for myIndex in newOrderNodes:
                            replaceNode = origNdList[myIndex]
                            NodeList[replaceCounter] = replaceNode
                            replaceCounter = replaceCounter + 1

                        # print("Original Tour")
                        # print(origNodeList)
                        # print("New Tour")
                        # print(newOrderNodes)

                        replaceTotalTourWeight = getTotalTourWeight(NodeList)

                    else: 
                        print("    NO SWAP!")
        
        compareEdgesCounter = compareEdgesCounter + 1

if __name__ == '__main__':

    print("\n***** Main *****\n")

    testNode1 = NodeStruct(0, 853, 85)
    testNode2 = NodeStruct(1, 622, 262)
    print("Edge weight between node1 and node2: ", getWeight(testNode1, testNode2))
    print("")

    cityList1 = []

    cityList1.append(NodeStruct(0, 200, 800))
    cityList1.append(NodeStruct(1, 3600, 2300))
    cityList1.append(NodeStruct(2, 3100, 3300))
    cityList1.append(NodeStruct(3, 4700, 5750))
    cityList1.append(NodeStruct(4, 5400, 5750))
    cityList1.append(NodeStruct(5, 5608, 7103))
    cityList1.append(NodeStruct(6, 4493, 7102))
    cityList1.append(NodeStruct(7, 3600, 6950))	

    mainTourEdgeList = generateTourEdgeList(cityList1)

    print("mainTourEdgeList length: ")
    print(len(mainTourEdgeList))
    print("printing mainTourEdgeList: ")
    print(mainTourEdgeList)
    print("")

    for edge in mainTourEdgeList:
        print(edge)
    print("")

    # print("mainTourEdgeList[7]:")
    # print(mainTourEdgeList[7])
    # print("")
    # mainTourEdgeList[7] = changeEdgeInfo(mainTourEdgeList[7], 10)
    # print("mainTourEdgeList[7] has changed.")
    # print(mainTourEdgeList[7])
    # print("")


    
    print("")
    
    # fileNm = "tsp_example_A.txt"
    # fileNm = "tsp_example_B.txt"
    # fileNm = "tsp_example_0.txt"
    fileNm = "tsp_example_1.txt"
    # fileNm = "tsp_example_2.txt"
    # fileNm = "test-input-1.txt"
    # fileNm = "test-input-1b.txt"
    
    workingNodeList = []
    getInput(fileNm, workingNodeList)
    inputNodeListStr = printNodeList(workingNodeList)
    print(workingNodeList)
    print("")
    
    origNodeList = []
    getInput(fileNm, origNodeList)
    origNdLstStr = printNodeList(origNodeList)
    print(origNodeList)    
    
    workingEdgeList = generateTourEdgeList(workingNodeList)
    print("workingEdgeList length: ")
    print(len(workingEdgeList))
    print("printing workingEdgeList: ")
    print(workingEdgeList)
    print("")

    for edge in workingEdgeList:
        print(edge)
    print("")    
    
    
    
    totalTourWeight = getTotalTourWeight(workingNodeList)
    print("Initial totalTourWeight: ")
    print(totalTourWeight)
    print("\n")    
        
        
        
    #Call Function
    # optimizePath()
    optimizePath(origNodeList, workingNodeList, workingEdgeList)
    
    print("\n\nMain: After running optimizePath(), workingNodeList: ")
    print(workingNodeList)
    
    # print("\nMain: NodeList:")
    # for node in NodeList:
    #     print(node.number)
    # print("\n")
    
    print("\nMain: Initial NodeList")
    print(inputNodeListStr)
    
    print("\nMain: Final NodeList")
    finalNodeListStr = printNodeList(workingNodeList)
    
    print ("\nFinal Edge List")
    print(workingEdgeList)
    
    print("\nOriginal Tour")
    print(origNodeList)
    
    origNdLstStr2 = printNodeList(origNodeList)
    
    print("Main: Initial totalTourWeight: ")
    print(totalTourWeight)
    
    finalTotalTourWeight = getTotalTourWeight(workingNodeList)
    print("Main: finalTotalTourWeight: ")
    print(finalTotalTourWeight)
    print("\n")        