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
eE = EdgeStruct(E, F, 0)
eF = EdgeStruct(F, G, 0)
eG = EdgeStruct(G, H, 0)
eH = EdgeStruct(H, A, 0)

#*********************
#End Test Data
#*********************

#PRINT INITIAL WEIGHT
print("Initial Total Weight")
totalWeight = getWeight(A, B) + getWeight(B, C) + getWeight(C, D) + getWeight(D, E) + getWeight(E, F) + getWeight(F, G) + getWeight(G, H) + getWeight(H, A)
print (totalWeight)


#List of Nodes and Edges Must Be in same order received From File
#NodeList Represents the Tour
NodeList = [A, B, C, D, E, F, G, H]
EdgeList = [eA, eB, eC, eD, eE, eF, eG, eH]
EdgeCount = len(EdgeList)

#Alters NodeList To a Better Tour
#Does Not Calculate Weight
#Need to Modularize Parts into seperate functions
def optimizePath():

    #Arbitray Number of Loops to compare each edge to all edges
    #increasing this loop from 1 to 2 improves final tour length 
    #we need to determine how many loops is optimal and if number of loops needs to be dynamic 
    compareEdgesCounter = 0
    while compareEdgesCounter < 2:
        #Double For loop means we are comparing the first edge against all edges then comparing second edge against all others etc.
        for edge1 in EdgeList:
            for edge2 in EdgeList:
                
                #Only do comparison edge1 and edge2 are not the same edge and are not 
                if( not(edge1.v1 == edge2.v1 or edge1.v1 == edge2.v2 or edge1.v2 == edge2.v1 or edge1.v2 == edge2.v2)):

                    #If the new set of edges are better than the existing ones, we need to reorder the vertexes of the NodeList because the tour has changed
                    #We do this by swapping the end vertex of the first edge and the start vertex of the second edge
                    #If we do this everytime edges are swapped, the nodelist stays up to date
                    #Before anything is altered, we need to get the NodeList index of the 1st edge's second vertex so that if we need to do the swap we can
                    indexOfSwapVertex1 = NodeList.index(edge1.v2)

                    #get cost of existing edges (edge pair that is currently in the tour)
                    existingWeight1 = getWeight(edge1.v1, edge1.v2)
                    existingWeight2 = getWeight(edge2.v1, edge2.v2)
                    existingTotal = (existingWeight1 + existingWeight2)

#******************
#This Section should be broken into its own section if we have time

                    # Need to determine which vertex needs to connect to which in order to create the new pair of edges
                    # Consider edge A-B and X-Y. When we remove these two edges, the tour will be divided into two seperate segments
                    # We know Vertex A should not connect to B because it was already connected to it.
                    # A could connect to X or Y.  A needs to connect to the vertex that is not in its segment.
                    # In order to make sure we do not connect A to the vertex in its same segment we look at the indexes of A, X, and Y in the NodeList
                    # A will connect to the the next node of either X or Y depending on which comes next in the tour. The vertex to come first has to be in the other segment

                    #initial vertexes of first edge and second edge
                    firstVertex = edge1.v1
                    secondVertex = edge1.v2

                    firstIndex = NodeList.index(firstVertex)
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
# ******************
                    #Get Weights of new edges
                    newWeight1 = getWeight(firstVertex, NodeList[FirstEdgeIndex])
                    newWeight2 = getWeight(secondVertex, NodeList[SecondEdgeIndex])
                    newTotal = (newWeight1 + newWeight2)

                    #if New edges are better, replace old edges
                    if(newTotal < existingTotal):

                        print ("\nReplace Fired!\n")

                        #Structs cannot be modified so the EdgeStructs Must be replaced

                        #create new edges
                        newEdge1 = EdgeStruct(edge1.v1, NodeList[FirstEdgeIndex], 0)
                        newEdge2 = EdgeStruct(edge2.v2, NodeList[SecondEdgeIndex], 0)

                        #get indexes of edges to replace
                        Edge1Index = EdgeList.index(edge1)
                        Edge2Index = EdgeList.index(edge2)

                        #set edge1 and edge2 to new values for loop
                        edge1 = newEdge1
                        edge2 = newEdge2

                        #Replace Edges in Edgelist
                        EdgeList[Edge1Index] = newEdge1
                        EdgeList[Edge2Index] = newEdge2

                        #Swap nodes in Node list so that NodeList is current and up to date
                        NodeList[indexOfSwapVertex1], NodeList[FirstEdgeIndex] = NodeList[FirstEdgeIndex], NodeList[indexOfSwapVertex1]

        compareEdgesCounter = compareEdgesCounter + 1


#Call Function
optimizePath()


#RESULT DATA
print ("Final Weights Are: ")
val1 = (getWeight(NodeList[0], NodeList[1]))
val2 = (getWeight(NodeList[1], NodeList[2]))
val3 = (getWeight(NodeList[2], NodeList[3]))
val4 = (getWeight(NodeList[3], NodeList[4]))
val5 = (getWeight(NodeList[4], NodeList[5]))
val6 = (getWeight(NodeList[5], NodeList[6]))
val7 = (getWeight(NodeList[6], NodeList[7]))
val8 = (getWeight(NodeList[7], NodeList[0]))

totalWeight = val1 + val2 + val3 + val4 + val5 + val6 + val7 + val8
print (totalWeight)

print(NodeList)