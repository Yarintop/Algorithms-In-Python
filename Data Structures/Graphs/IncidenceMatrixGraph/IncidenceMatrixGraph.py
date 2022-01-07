from IncidenceMatrixGraphNode import IncidenceMatrixGraphNode
from IncidenceMatrixGraphEdge import IncidenceMatrixGraphEdge

class IncidenceMatrixGraph:
    def __init__(self) -> None:
        self._matrix = []
        self._nodes = []
        self._edges = []

    def adjacent(self, nodeA, nodeB):
        for e in self._edges:
            if self._matrix[nodeA.index][e.index] and self._matrix[nodeB.index][e.index]:
                return True
        return False

    def neighbors(self, node):
        neighbors = []
        for e in self._edges:
            if not self._matrix[node.index][e.index]:
                continue
            
            for n in self._nodes:
                if n == node:
                    continue
                if self._matrix[n.index][e.index]:
                    neighbors.append(n)
                    break
            else:
                raise ValueError("A node cannot be connected to an edge alone.")
        return neighbors

    def addNode(self, node):
        if node not in self._nodes:
            self._matrix.append([0] * len(self._edges))
            self._nodes.append(node)

    def removeNode(self, node):
        self._matrix.pop(node.index)
        self._nodes.remove(node)
        for n in self._nodes[node.index + 1:]:
            n.index -= 1

    def addEdge(self, nodeA, nodeB, directional=False):
        for i in range(len(self._nodes)):
            self._matrix[i].append(0)
            
        e = IncidenceMatrixGraphEdge(len(self._edges))
        self._edges.append(e)

        self._matrix[nodeA.index][e.index] = 1
        self._matrix[nodeB.index][e.index] = 1
            
    def removeEdge(self, nodeA, nodeB, directional=False):
        for edge in self._edges:
            if self._matrix[nodeA.index][edge.index] and self._matrix[nodeA.index][edge.index]:
                e = edge
                
        for i in range(len(self._nodes)):
            self._matrix[i].pop(e.index)
            
        self._edges.remove(e)
        

if __name__ == "__main__":
    graph = IncidenceMatrixGraph()
    
