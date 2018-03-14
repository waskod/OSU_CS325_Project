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
from collections import namedtuple


NodeStruct = namedtuple("NodeStruct", "number x y")

EdgeStruct = namedtuple("EdgeStruct", "id startNode endNode weight")


# =====================================================================
# Functions
# =====================================================================
def getWeight(node1, node2):
    weight = math.hypot(node1.x - node2.x, node1.y - node2.y)
    return weight

	
def changeEdgeInfo(edgeStrct, newEndNodeNum):
    startNodeNum = edgeStrct.startNode
    newIdStr = str(startNodeNum) + "_" + str(newEndNodeNum)
    edgeStrct = edgeStrct._replace(id = newIdStr, endNode = newEndNodeNum)
    return edgeStrct
	
	
def generateTourEdgeList(cityList):
    tourEdgeList = []
    lenCList = len(cityList)

    for i in range(0, lenCList - 1):
        idStr = str(cityList[i].number) + "_" + str(cityList[i + 1].number)
        newEdge = EdgeStruct(idStr, cityList[i].number, cityList[i + 1].number, 0)
        tourEdgeList.append(newEdge)

    # Add the last edge connecting last node to origin node
    lastIdStr = str(cityList[lenCList - 1].number) + "_" + str(cityList[0].number)
    lastEdge = EdgeStruct(lastIdStr, cityList[lenCList - 1].number, cityList[0].number, 0)
    tourEdgeList.append(lastEdge)

    return tourEdgeList


if __name__ == '__main__':

    print ""
    print "***** Main *****"
    print ""

    testNode1 = NodeStruct(0, 853, 85)
    testNode2 = NodeStruct(1, 622, 262)
    print "Edge weight between node1 and node2: ", getWeight(testNode1, testNode2)
	
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
   
    print "mainTourEdgeList length: "
    print(len(mainTourEdgeList))
    print "printing mainTourEdgeList: "
    print(mainTourEdgeList)
    print ""

    for edge in mainTourEdgeList:
        print(edge)
    print ""

    print "mainTourEdgeList[7]:"
    print(mainTourEdgeList[7])
    print ""

    mainTourEdgeList[7] = changeEdgeInfo(mainTourEdgeList[7], 10)
   
    print "mainTourEdgeList[7] has changed."
    print(mainTourEdgeList[7])
    print ""		
	
	
	
	
	
	