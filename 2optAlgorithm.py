import sys
import math
from collections import namedtuple

NodeStruct = namedtuple("NodeStruct", "number x y")

def getWeight(node1, node2):
    weight = math.hypot(node1.x - node2.x, node1.y - node2.y)
    return int(round(weight))

#Node Struct id, xaxis, yaxis
A = NodeStruct(0, 1, 1)
B = NodeStruct(1, 5, 1)
C = NodeStruct(2, 8, 6)
D = NodeStruct(3, 4, 2)
E = NodeStruct(4, 1, 6)

NodeList = [A, B, C, D, E]

#EdgeStruct start vertex, end vertex weight
EdgeStruct = namedtuple("EdgeStruct", "v1 v2 weight")

eA = EdgeStruct(A, B, 0)
eB = EdgeStruct(B, C, 0)
eC = EdgeStruct(C, D, 0)
eD = EdgeStruct(D, E, 0)
eE = EdgeStruct(E, A, 0)

EdgeList = [eA, eB, eC, eD, eE]
EdgeCount = len(EdgeList)
def optimizePath():

    for edge1 in EdgeList:
        for edge2 in EdgeList:
            #Only Execute if not the same edge and not adjacent
            if( not(edge1.v1 == edge2.v1 or edge1.v1 == edge2.v2 or edge1.v2 == edge2.v1 or edge1.v2 == edge2.v2)):
                #print edge2

                FirstIndex = NodeList.index(edge1.v2)

                #get cost of exiting edges
                existingWeight1 = getWeight(edge1.v1, edge1.v2)
                existingWeight2 = getWeight(edge2.v1, edge2.v2)
                existingTotal = (existingWeight1 + existingWeight2)
                #print existingTotal

                #determine which nodes the nodes of the first edge will connect to
                #need to ensure, node does not connect to node from other edge that is in its subset
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
                #firstEdgeIndex = new vertex index in nodelist

                newWeight1 = getWeight(firstVertex, NodeList[FirstEdgeIndex])
                newWeight2 = getWeight(secondVertex, NodeList[SecondEdgeIndex])
                newTotal = (newWeight1 + newWeight2)

                if(newTotal < existingTotal):

                    print EdgeList
                    #store a temp
                    #TempNode = NodeStruct(edge1.v2.number, edge1.v2.x, edge1.v2.y)
                    newEdge1 = EdgeStruct(edge1.v1, NodeList[FirstEdgeIndex], 0)#EdgeStruct start vertex, end vertex weight
                    newEdge2 = EdgeStruct(edge2.v2, NodeList[SecondEdgeIndex], 0)

                    Edge1Index = EdgeList.index(edge1)
                    Edge2Index = EdgeList.index(edge2)

                    edge1 = newEdge1
                    edge2 = newEdge2

                    EdgeList[Edge1Index] = newEdge1
                    EdgeList[Edge2Index] = newEdge2

                    #need to flip values
                    SecondIndex = NodeList.index(edge1.v2)

                    NodeList[firstIndex], NodeList[SecondIndex] = NodeList[SecondIndex], NodeList[firstIndex]
 ##                  NodeList[FirstIndex], NodeList[SecondIndex] = NodeList[SecondIndex], NodeList[FirstIndex]
                    #order tour to be correct



optimizePath()


print NodeList