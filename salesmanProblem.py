# ====================================================================
# Authors:
# Michael Tucker              tuckemic@oregonstate.edu    ID:
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


# =====================================================================
# Functions
# =====================================================================
def getWeight(node1, node2):
    weight = math.hypot(node1.x - node2.x, node1.y - node2.y)
    return weight


if __name__ == '__main__':
    testNode1 = NodeStruct(0, 853, 85)
    testNode2 = NodeStruct(1, 622, 262)
    print "Edge weight between node1 and node2: ", getWeight(testNode1, testNode2)