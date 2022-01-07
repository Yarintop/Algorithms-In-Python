from IncidenceMatrixGraphNode import IncidenceMatrixGraphNode
from IncidenceMatrixGraphEdge import IncidenceMatrixGraphEdge

class IncidenceMatrixGraph:
    def __init__(self) -> None:
        self.matrix = []
        self.nodes = []
        self.edges = []

    def adjacent(self, nodeA, nodeB):
        for e in self.edges:
            if self.matrix[nodeA.index][e.index] and self.matrix[nodeB.index][e.index]:
                return True
        return False

    def neighbors(self, node):
        neighbors = []
        for e in self.edges:
            if not self.matrix[node.index][e.index]:
                continue
            
            for n in self.nodes:
                if n == node:
                    continue
                if self.matrix[n.index][e.index]:
                    neighbors.append(n)
                    break
            else:
                raise ValueError("A node cannot be connected to an edge alone.")
        return neighbors

    def addNode(self, node):
        if node not in self.nodes:
            node.index = len(self.nodes)
            self.matrix.append([0] * len(self.edges))
            self.nodes.append(node)

    def removeNode(self, node):
        neighbors = self.neighbors(node)
        for n in neighbors:
            self.removeEdge(node, n)
                
        self.matrix.pop(node.index)
        self.nodes.remove(node)
        for n in self.nodes[node.index:]:
            n.index -= 1

    def addEdge(self, nodeA, nodeB):
        for i in range(len(self.nodes)):
            self.matrix[i].append(0)
            
        e = IncidenceMatrixGraphEdge(len(self.edges))
        self.edges.append(e)

        self.matrix[nodeA.index][e.index] = 1
        self.matrix[nodeB.index][e.index] = 1
            
    def removeEdge(self, nodeA, nodeB):
        edges = []
        for edge in self.edges:
            if self.matrix[nodeA.index][edge.index] and self.matrix[nodeB.index][edge.index]:
                edges.append(edge)
                
        edges.sort(key=lambda e: e.index, reverse=True)
        for edge in edges:
            for i in range(len(self.nodes)):
                self.matrix[i].pop(edge.index)
            
            self.edges.remove(edge)
            
            for e in self.edges[edge.index:]:
                e.index -= 1
        

if __name__ == "__main__":
    graph = IncidenceMatrixGraph()
    
    a = IncidenceMatrixGraphNode(5)
    b = IncidenceMatrixGraphNode(20)
    c = IncidenceMatrixGraphNode(15)
    d = IncidenceMatrixGraphNode(9)
    
    graph.addNode(a)
    graph.addNode(b)
    graph.addNode(c)
    graph.addNode(d)
    
    print(graph.nodes)
    print(graph.edges)
    
    graph.addEdge(a, b)
    graph.addEdge(b, d)
    graph.addEdge(b, c)
    
    print(graph.edges)
    
    print(graph.adjacent(b, a))
    print(graph.adjacent(c, d))
    
    graph.removeNode(a)
    
    print(graph.nodes)

    print(graph.neighbors(b))
