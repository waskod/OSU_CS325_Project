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

# A = NodeStruct(0, 1, 1)
# B = NodeStruct(1, 5, 1)
# C = NodeStruct(2, 8, 6)
# D = NodeStruct(3, 4, 2)
# E = NodeStruct(4, 1, 6)


#Test Nodes
A = NodeStruct(0, 485, 6238)
B = NodeStruct(1, 11, 2579)
C = NodeStruct(2, 1651, 4220)
D = NodeStruct(3, 74, 1493)
E = NodeStruct(4, 1, 1)
F = NodeStruct(5, 1959, 33)
G = NodeStruct(6, 1, 56)
H = NodeStruct(7, 4659, 563)


# A = NodeStruct(0, 200, 800)
# B = NodeStruct(1, 3600, 2300)
# C = NodeStruct(2, 3100, 3300)
# D = NodeStruct(3, 4700, 5750)
# E = NodeStruct(4, 5400, 5750)
# F = NodeStruct(5, 5608, 7103)
# G = NodeStruct(6, 4493, 7102)
# H = NodeStruct(7, 3600, 6950)


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

#PRINT INITIAL WEIGHT
print("\nInitial Total Weight")
totalWeight = getWeight(A, B) + getWeight(B, C) + getWeight(C, D) + getWeight(D, E) + getWeight(E, F) + getWeight(F, G) + getWeight(G, H) + getWeight(H, A)
# totalWeight = getWeight(A, B) + getWeight(B, C) + getWeight(C, D) + getWeight(D, E) + getWeight(E, A)
print (totalWeight)
print("\n")


#List of Nodes and Edges Must Be in same order received From File
#NodeList Represents the Tour
NodeList = [A, B, C, D, E, F, G, H]
# NodeList = [A, B, C, D, E]
NodeCount = len(NodeList)


totalTourWeight = getTotalTourWeight(NodeList)
print("Initial totalTourWeight: ")
print(totalTourWeight)
print("\n")


print("\nInitial NodeList")
initialNodeListStr = printNodeList(NodeList)


EdgeList = [eA, eB, eC, eD, eE, eF, eG, eH]
# EdgeList = [eA, eB, eC, eD, eE]
EdgeCount = len(EdgeList)


  

#Alters NodeList To a Better Tour
#Does Not Calculate Weight
#Need to Modularize Parts into seperate functions

def optimizePath():

    numCycles = 3


    totalTourWeight = getTotalTourWeight(NodeList)
    print("Initial totalTourWeight: ")
    print(totalTourWeight)
    print("\n")

    #Arbitray Number of Loops to compare each edge to all edges
    #increasing this loop from 1 to 2 improves final tour length 
    #we need to determine how many loops is optimal and if number of loops needs to be dynamic 
    compareEdgesCounter = 0
    swapCount = 0
    while compareEdgesCounter < numCycles:
        print("\nOuter while loop. compareEdgesCounter: " + str(compareEdgesCounter))
        print("                            swapCount: " + str(swapCount) + "\n")
        
        #Double For loop means we are comparing the first edge against all edges then comparing second edge against all others etc.
        for edge1 in EdgeList:
            
            edge1Str = createVtxPairFromEStrct(edge1)
            print("\n\n **********************************************************************************************")
            print("\n  Outer For Loop:  edge1: " + edge1Str)            
            
            for edge2 in EdgeList:

                #Only do comparison edge1 and edge2 are not the same edge and are not 
                if( not(edge1.v1 == edge2.v1 or edge1.v1 == edge2.v2 or edge1.v2 == edge2.v1 or edge1.v2 == edge2.v2)):

                    edge2Str = createVtxPairFromEStrct(edge2)
                    print("\n\n **********************************************************************************************")
                    print(" compareEdgesCounter: " + str(compareEdgesCounter))
                    print(" swapCount: " + str(swapCount))
                    print(" edge1: " + edge1Str) 
                    print("\n    Inner For Loop:  edge2: " + edge2Str)                     

                    #If the new set of edges are better than the existing ones, we need to reorder the vertexes of the NodeList because the tour has changed
                    #We do this by swapping the end vertex of the first edge and the start vertex of the second edge
                    #If we do this everytime edges are swapped, the nodelist stays up to date
                    #Before anything is altered, we need to get the NodeList index of the 1st edge's second vertex so that if we need to do the swap we can
                    indexOfSwapVertex1 = NodeList.index(edge1.v2)
                    print("    indexOfSwapVertex1: " + str(indexOfSwapVertex1))

                    #get cost of existing edges (edge pair that is currently in the tour)
                    existingWeight1 = getWeight(edge1.v1, edge1.v2)
                    existingWeight2 = getWeight(edge2.v1, edge2.v2)
                    existingTotal = (existingWeight1 + existingWeight2)

                    existingEdgePairStr = edge1Str + " " + edge2Str
                    print("    Existing edge pair: " + existingEdgePairStr)
                    print("    Existing total weight: " + str(existingTotal))
                    
                    


#******************
#This Section should be broken into its own section if we have time

                    # Need to determine which vertex needs to connect to which in order to create the new pair of edges
                    # Consider edge A-B and X-Y. When we remove these two edges, the tour will be divided into two seperate segments
                    # We know Vertex A should not connect to B because it was already connected to it.
                    # A could connect to X or Y.  A needs to connect to the vertex that is not in its segment.
                    # In order to make sure we do not connect A to the vertex in its same segment we look at the indexes of A, X, and Y in the NodeList
                    # A will connect to the the next node of either X or Y depending on which comes next in the tour. The vertex to come first has to be in the other segment

                    print("\n    Starting index calculations.\n")

                    #initial vertexes of new first edge and second edge
                    firstVertex = edge1.v1
                    secondVertex = edge1.v2
                    
                    """
                    # New Code to handle edge pair case of higher v1 number first in pair
                    e1v1 = edge1.v1.number
                    e1v2 = edge1.v2.number
                    
                    e2v1 = edge2.v1.number
                    e2v2 = edge2.v2.number
                    
                    print("    e1v1, e1v2: " + str(e1v1) + ", " + str(e1v2))
                    print("    e2v1, e2v2: " + str(e2v1) + ", " + str(e2v2))
                    
                    if e2v1 < e1v1:
                        firstVertex = edge2.v1
                        secondVertex = edge2.v2
                        print("    IF: firstVertex.number: " + str(firstVertex.number))
                        print("    IF: secondVertex.number: " + str(secondVertex.number))                        
                    else:
                        firstVertex = edge1.v1
                        secondVertex = edge1.v2                    
                        print("    ELSE: firstVertex.number: " + str(firstVertex.number))
                        print("    ELSE: secondVertex.number: " + str(secondVertex.number))
                    """

                    firstIndex = NodeList.index(firstVertex)

                    """
                    # New Code
                    if e2v1 < e1v1:
                        p1Index = NodeList.index(edge1.v1)
                        p2Index = NodeList.index(edge1.v2)
                        print("    IF: p1Index: " + str(p1Index))
                        print("    IF: p2Index: " + str(p2Index))
                    else: 
                        p1Index = NodeList.index(edge2.v1)
                        p2Index = NodeList.index(edge2.v2)
                        print("    ELSE: p1Index: " + str(p1Index))
                        print("    ELSE: p2Index: " + str(p2Index))
                    """    
                    
                    p1Index = NodeList.index(edge2.v1)
                    p2Index = NodeList.index(edge2.v2)                        
                        

                    if( (firstIndex < p1Index and firstIndex < p2Index) and (firstIndex > p1Index and firstIndex > p2Index)):
                        if( p1Index< p2Index):
                            FirstEdgeIndex = p1Index
                            SecondEdgeIndex = p2Index
                        else:
                            FirstEdgeIndex = p2Index
                            SecondEdgeIndex = p1Index
                            
                    elif( firstIndex < p1Index):
                        FirstEdgeIndex = p1Index
                        SecondEdgeIndex = p2Index
                        
                    else:
                        FirstEdgeIndex = p2Index
                        SecondEdgeIndex = p1Index
                        
                        
                    print("\n    Finished with index calculations.\n")
                        
# ******************

                    print("\n    After index calculations section. New edge stats: ")
                    
                    
                    print("\n    firstVertex:              " + str(firstVertex))
                    # print("    FirstEdgeIndex: " + str(FirstEdgeIndex))
                    print("    NodeList[FirstEdgeIndex]: " + str(NodeList[FirstEdgeIndex]))
                    
                    newE1Vtx1 = firstVertex.number
                    newE1Vtx2 = NodeList[FirstEdgeIndex].number
                    
                    print("\n    secondVertex:              " + str(secondVertex))
                    # print("    SecondEdgeIndex: " + str(SecondEdgeIndex))
                    print("    NodeList[SecondEdgeIndex]: " + str(NodeList[SecondEdgeIndex]))
                    
                    newE2Vtx1 = secondVertex.number
                    newE2Vtx2 = NodeList[SecondEdgeIndex].number                    
                                      
                                      
                    #Get Weights of new edges            
                    newWeight1 = getWeight(firstVertex, NodeList[FirstEdgeIndex])
                    newWeight2 = getWeight(secondVertex, NodeList[SecondEdgeIndex])
                    newTotal = (newWeight1 + newWeight2)

                    
                    
                    newEdge1Str = "(" + str(newE1Vtx1) + ", " + str(newE1Vtx2) + ")"
                    # newEdge1Str = "(#, #)"
                    print("\n    new edge1: " + newEdge1Str)
                    
                    newEdge2Str = "(" + str(newE2Vtx1) + ", " + str(newE2Vtx2) + ")"
                    # newEdge2Str = "(#, #)"
                    # newEdge2Str = createVtxPairFromEStrct(edge2)
                    print("    new edge2: " + newEdge2Str)

                    newEdgePairStr = newEdge1Str + " " + newEdge2Str
                    print("    New edge pair: " + newEdgePairStr)
                    print("    New total weight: " + str(newTotal))
                    print("    Existing total weight: " + str(existingTotal))


# ******************

                    #if New edges are better, replace old edges
                    if(newTotal < existingTotal):

                        print("\n\n      **********************************************************************************************")
                        print("      ##############################################################################################")
                        print("      *********************************************************************************************")
                        print ("\n      ********** Replace Fired! **********\n")

                        swapCount += 1


                        #Structs cannot be modified so the EdgeStructs Must be replaced

                        #create new edges
                        # newEdge1 = EdgeStruct(edge1.v1, NodeList[FirstEdgeIndex], 0)
                        # newEdge2 = EdgeStruct(edge2.v2, NodeList[SecondEdgeIndex], 0)

                        # print("      Creating new edges:")
                        # print("      edge1.v1: " + str(edge1.v1))
                        # print("      NodeList[FirstEdgeIndex]: " + str(NodeList[FirstEdgeIndex]) + "\n")
 

                        # New code
                        
                        newEdge1 = EdgeStruct(firstVertex, NodeList[FirstEdgeIndex], 0)                
                        newEdge2 = EdgeStruct(secondVertex, NodeList[SecondEdgeIndex], 0)

                        
                        print("      Creating new edges:")
                        newEdge1Str = createVtxPairFromEStrct(newEdge1)
                        print("      newEdge1: " + newEdge1Str)
                        newEdge2Str = createVtxPairFromEStrct(newEdge2)
                        print("      newEdge2: " + newEdge2Str)                        


                        #get indexes of edges to replace
                        Edge1Index = EdgeList.index(edge1)
                        Edge2Index = EdgeList.index(edge2)
                        
                        print("\n      Indexes of edges to replace")
                        print("      Edge1Index: " + str(Edge1Index))
                        print("      Edge2Index: " + str(Edge2Index))


                        #set edge1 and edge2 to new values for loop
                        edge1 = newEdge1
                        edge2 = newEdge2
                        
                        print("\n      New values for edge1 and edge2 for loop")
                        newValEdge1Str = createVtxPairFromEStrct(edge1)
                        print("      newValEdge1: " + newValEdge1Str)
                        newValEdge2Str = createVtxPairFromEStrct(edge2)
                        print("      newValEdge2: " + newValEdge2Str)                         
                        

                        #Replace Edges in Edgelist
                        EdgeList[Edge1Index] = newEdge1
                        EdgeList[Edge2Index] = newEdge2
                        
                        print("\n      EdgeList replacements.")
                        newEdgeList1Str = createVtxPairFromEStrct(EdgeList[Edge1Index])
                        print("      newEdgeList1Str: " + newEdgeList1Str)
                        newEdgeList2Str = createVtxPairFromEStrct(EdgeList[Edge2Index])
                        print("      newEdgeList2Str: " + newEdgeList2Str)                         
                        

                        #Swap nodes in Node list so that NodeList is current and up to date
                        NodeList[indexOfSwapVertex1], NodeList[FirstEdgeIndex] = NodeList[FirstEdgeIndex], NodeList[indexOfSwapVertex1]
                        
                        print("\n      End of Replace Portion. NodeList: ")
                        printNodeList(NodeList)
                        
                        print("      previous totalTourWeight: " + str(totalTourWeight))
                        replaceTotalTourWeight = getTotalTourWeight(NodeList)
                        print("      replaceTotalTourWeight: ")
                        print(replaceTotalTourWeight)
                        totalTourWeight = replaceTotalTourWeight
                        print("\n")                        
                        
                    else: 
                        print("    NO SWAP!")
                        printNodeList(NodeList)
                                            

        iterTotalTourWeight = getTotalTourWeight(NodeList)
        print("\nwhile iter: " + str(compareEdgesCounter) + ":  iterTotalTourWeight: ")
        print(iterTotalTourWeight)
        print("\n")        
        
        compareEdgesCounter = compareEdgesCounter + 1

    print("\noptimizePath() function ending. numCycles: " + str(numCycles))
    print("\noptimizePath() function ending. Final swapCount: " + str(swapCount) + "\n")          
              

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


#RESULT DATA
print ("Main: Comparing Starting and Final Weights: ")
val1 = (getWeight(NodeList[0], NodeList[1]))
val2 = (getWeight(NodeList[1], NodeList[2]))
val3 = (getWeight(NodeList[2], NodeList[3]))
val4 = (getWeight(NodeList[3], NodeList[4]))
# val5 = (getWeight(NodeList[4], NodeList[0]))
val5 = (getWeight(NodeList[4], NodeList[5]))
val6 = (getWeight(NodeList[5], NodeList[6]))
val7 = (getWeight(NodeList[6], NodeList[7]))
val8 = (getWeight(NodeList[7], NodeList[0]))


print("Main: Starting totalWeight:  " + str(totalWeight) + "\n")

finalTotalTourWeight = getTotalTourWeight(NodeList)
print("Main: finalTotalTourWeight: ")
print(finalTotalTourWeight)

# newTotalWeight = val1 + val2 + val3 + val4 + val5
newTotalWeight = val1 + val2 + val3 + val4 + val5 + val6 + val7 + val8
# print (newTotalWeight)
print("Main:       newTotalWeight:  " + str(newTotalWeight) + "\n")




