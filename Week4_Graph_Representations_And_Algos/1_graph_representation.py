"""
Two methods of Graph Representation
1. Adjecency Matrix          2. Adjecency List
"""

"""
Adjacency Matrix
"""
import numpy as np
def getAdjacencyMatrix(V, E):
    size = len(V)
    adjMatrix = np.zeros(shape=(size,size))
    for (u,v) in E:
        adjMatrix[u][v] = 1
    return adjMatrix

def getAdjacencyList(V,E):
    size = len(V)
    adjList = {}
    for i in range(size):
        adjList[i] = []
    for (u,v) in E:
        adjList[u].append(v)
    return adjList

V=[0,1,2,3,4]
E=[(0,1),(0,3),(2,3),(1,4),(3,4)]
print(getAdjacencyMatrix(V,E))
print(getAdjacencyList(V,E))