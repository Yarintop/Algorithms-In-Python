from AdjacencyListGraphNode import AdjacencyListGraphNode


class AdjacencyListGraph:
    def __init__(self) -> None:
        self.nodes = []

    def adjacent(self, nodeA, nodeB):
        return nodeB in nodeA.neighbors

    def neighbors(self, node):
        return node.neighbors

    def addNode(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def removeNode(self, node):
        self.nodes.remove(node)
        for n in node.neighbors:
            n.neighbors.remove(node)

    def addEdge(self, nodeA, nodeB, directional=False):
        nodeA.neighbors.append(nodeB)
        if not directional:
            nodeB.neighbors.append(nodeA)
            

    def removeEdge(self, nodeA, nodeB, directional=False):
        self.nodeA.neighbors.remove(nodeB)
        if not directional:
            self.nodeB.neighbors.remove(nodeA)
        

if __name__ == "__main__":
    graph = AdjacencyListGraph()
    
    a = AdjacencyListGraphNode(5)
    b = AdjacencyListGraphNode(20)
    c = AdjacencyListGraphNode(15)
    d = AdjacencyListGraphNode(9)
    
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