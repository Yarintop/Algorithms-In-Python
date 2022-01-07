from AdjacencyMatrixGraphNode import AdjacencyMatrixGraphNode

class AdjacencyMatrixGraph:
    def __init__(self) -> None:
        self.matrix = []
        self.nodes = []

    def adjacent(self, nodeA, nodeB):
        i = nodeA.index
        j = nodeB.index
        if self.matrix[i][j] or self.matrix[j][i]:
            return True
        return False

    def neighbors(self, node):
        neighbors = []
        i = node.index
        for j in range(len(self.matrix[i])):
            if self.matrix[i][j]:
                neighbors.append(self.nodes[j])
        return neighbors

    def addNode(self, node):
        if node not in self.nodes:
            for i in range(len(self.nodes)):
                self.matrix[i].append(0)
            
            node.index = len(self.matrix)
            self.matrix.append([0] * (len(self.matrix) + 1))
            self.nodes.append(node)

    def removeNode(self, node):
        for i in range(len(self.nodes)):
            self.matrix[i].pop(node.index)
            
        self.matrix.pop(node.index)
        self.nodes.remove(node)
        for n in self.nodes[node.index:]:
            n.index -= 1
            

    def addEdge(self, nodeA, nodeB, directional=False):
        self.matrix[nodeA.index][nodeB.index] = 1
        if not directional:
            self.matrix[nodeB.index][nodeA.index] = 1
            
    def removeEdge(self, nodeA, nodeB, directional=False):
        self.matrix[nodeA.index][nodeB.index] = 0
        if not directional:
            self.matrix[nodeB.index][nodeA.index] = 0
        

if __name__ == "__main__":
    graph = AdjacencyMatrixGraph()
    
    a = AdjacencyMatrixGraphNode(5)
    b = AdjacencyMatrixGraphNode(20)
    c = AdjacencyMatrixGraphNode(15)
    d = AdjacencyMatrixGraphNode(9)
    
    graph.addNode(a)
    graph.addNode(b)
    graph.addNode(c)
    graph.addNode(d)
    
    print(graph.nodes)
    
    graph.addEdge(a, b)
    graph.addEdge(b, d)
    graph.addEdge(b, c)
    
    print(graph.adjacent(b, a))
    print(graph.adjacent(c, d))
    
    graph.removeNode(a)
    
    print(graph.nodes)

    print(graph.neighbors(b))