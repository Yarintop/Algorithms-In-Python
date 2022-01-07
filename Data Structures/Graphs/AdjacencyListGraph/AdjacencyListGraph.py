from AdjacencyListGraphNode import AdjacencyListGraphNode


class AdjacencyListGraph:
    def __init__(self) -> None:
        self.nodes = []

    def adjacent(self, nodeA, nodeB):
        return nodeB in nodeA.neighbors

    def neighbors(self, node):
        return self.neighbors.copy()

    def addNode(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def removeNode(self, node):
        self.nodes.remove(node)
        for n in node.neighbors:
            n.neighbors.remove(node)

    def addEdge(self, nodeA, nodeB, directional=False):
        self.nodeA.neighbors.append(nodeB)
        if not directional:
            self.nodeB.neighbors.append(nodeA)
            

    def removeEdge(self, nodeA, nodeB, directional=False):
        self.nodeA.neighbors.remove(nodeB)
        if not directional:
            self.nodeB.neighbors.remove(nodeA)
        

if __name__ == "__main__":
    graph = AdjacencyListGraph()
    
