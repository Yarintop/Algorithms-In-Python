from AdjacencyMatrixGraphNode import AdjacencyMatrixGraphNode

class AdjacencyMatrixGraph:
    def __init__(self) -> None:
        self._matrix = []
        self._nodes = []

    def adjacent(self, nodeA, nodeB):
        i = nodeA.index
        j = nodeB.index
        return self._matrix[i][j] or self._matrix[j][i]

    def neighbors(self, node):
        neighbors = []
        i = node.index
        for j in range(len(self._matrix[i])):
            if self._matrix[i][j]:
                neighbors.append(self._nodes[j])

    def addNode(self, node):
        for i in range(len(self._nodes)):
            self._matrix[i].append(0)
            
        if node not in self._nodes:
            self._matrix.append([0] * (len(self._matrix) + 1))
            self._nodes.append(node)

    def removeNode(self, node):
        for i in range(len(self._nodes)):
            self._matrix[i].pop(node.index)
            
        self._matrix.pop(node.index)
        self._nodes.remove(node)
        for n in self._nodes[node.index + 1:]:
            n.index -= 1
            

    def addEdge(self, nodeA, nodeB, directional=False):
        self._matrix[nodeA.index][nodeB.index] = 1
        if not directional:
            self._matrix[nodeB.index][nodeA.index] = 1
            
    def removeEdge(self, nodeA, nodeB, directional=False):
        self._matrix[nodeA.index][nodeB.index] = 0
        if not directional:
            self._matrix[nodeB.index][nodeA.index] = 0
        

if __name__ == "__main__":
    graph = AdjacencyMatrixGraph()
    
