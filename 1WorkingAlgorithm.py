import sys
import math
from collections import namedtuple

#Node Struct stores vertices EdgeStruct Stores Edges

#Values : Id Number, X Vertex, Y Vertex
NodeStruct = namedtuple("NodeStruct", "number x y")

#Values: Start Vertex, End Vertex, Weight
EdgeStruct = namedtuple("EdgeStruct", "v1 v2 weight")

#Get Distance Between two nodes rounded to the nearest integer
def getWeight(node1, node2):
    weight = math.hypot(node1.x - node2.x, node1.y - node2.y)
    return int(round(weight))

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
    # print(edgeStr)
    return edgeStr

def printNodeList(nodeList):
    # nodeCount = lenNodeList
    # for i in range(0, nodeCount):
    nodeStr = ""
    for node in NodeList:
        # print(node.number)        
        nodeStr += str(node.number)
        nodeStr += ", "
    nodeStr2 = nodeStr.rstrip(', ')
    nodeStr2 += "\n"
    print(nodeStr2)
    return nodeStr2
    

#*********************
#TEST DATA
#*********************

#Test Nodes
A = NodeStruct(0, 485, 6238)
B = NodeStruct(1, 11, 2579)
C = NodeStruct(2, 1651, 4220)
D = NodeStruct(3, 74, 1493)
E = NodeStruct(4, 1, 1)
F = NodeStruct(5, 1959, 33)
G = NodeStruct(6, 1, 56)
H = NodeStruct(7, 4659, 563)

#Test Edges
eA = EdgeStruct(A, B, 0)
eB = EdgeStruct(B, C, 0)
eC = EdgeStruct(C, D, 0)
eD = EdgeStruct(D, E, 0)
# eE = EdgeStruct(E, A, 0)  # for set of 5 nodes case
eE = EdgeStruct(E, F, 0)
eF = EdgeStruct(F, G, 0)
eG = EdgeStruct(G, H, 0)
eH = EdgeStruct(H, A, 0)
#*********************
#End Test Data
#*********************

#List of Nodes and Edges Must Be in same order received From File
#NodeList Represents the Tour
origNodeList = [A, B, C, D, E, F, G, H]
NodeList = [A, B, C, D, E, F, G, H]
NodeCount = len(NodeList)

totalTourWeight = getTotalTourWeight(NodeList)
print("Initial totalTourWeight: ")
print(totalTourWeight)
print("\n")

print("\nInitial NodeList")
initialNodeListStr = printNodeList(NodeList)

EdgeList = [eA, eB, eC, eD, eE, eF, eG, eH]
EdgeCount = len(EdgeList)

#Alters NodeList To a Better Tour
#Does Not Calculate Weight
#Need to Modularize Parts into seperate functions

def optimizePath():

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
                        print(newOrderNodes)
                            
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

                            print "New Order Nodes and List of Edges"
                            print(newOrderNodes)
                            print(listofEdges)

                        print "Nodes Going In"
                        print newOrderNodes

                        replaceCounter = 0
                        for myIndex in newOrderNodes:
                            replaceNode = origNodeList[myIndex]
                            NodeList[replaceCounter] = replaceNode
                            replaceCounter = replaceCounter + 1

                        print("Original Tour")
                        print origNodeList
                        print ("New Tour")
                        print newOrderNodes

                        replaceTotalTourWeight = getTotalTourWeight(NodeList)

                    else: 
                        print("    NO SWAP!")
        
        compareEdgesCounter = compareEdgesCounter + 1

#Call Function
optimizePath()

print("\n\nMain: After running optimizePath(), NodeList: ")
print(NodeList)

# print("\nMain: NodeList:")
# for node in NodeList:
#     print(node.number)
# print("\n")

print("\nMain: Initial NodeList")
print(initialNodeListStr)

print("\nMain: Final NodeList")
finalNodeListStr = printNodeList(NodeList)

print ("\nFinal Edge List")
print EdgeList

print("Original Tour")
print origNodeList

finalTotalTourWeight = getTotalTourWeight(NodeList)
print("Main: finalTotalTourWeight: ")
print(finalTotalTourWeight)