from GraphEdge import GraphEdge
from GraphNode import GraphNode


class Graph:
    def __init__(self) -> None:
        self.nodes = []
        self.edges = []

    def adjacent(self, nodeA, nodeB):
        return any(nodeA in e.getNodes() and nodeB in e.getNodes() for e in self.edges)

    def neighbors(self, node):
        neighbors = []
        nodeEdges = [e for e in self.edges if node in e.getNodes()]
        for e in nodeEdges:
            if node == e.start:
                neighbors.append(e.end)
            elif not e.directional:
                neighbors.append(e.start)
                
        return list(set(neighbors))

    def addNode(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def removeNode(self, node):
        self.nodes.remove(node)
        self.edges = list(filter(lambda e: node not in e.getNodes(), self.edges))

    def addEdge(self, nodeA, nodeB, directional=False):
        self.edges.append(GraphEdge(nodeA, nodeB, directional))

    def removeEdge(self, nodeA, nodeB, directional=False):
        if not directional:
            filterFunction = lambda e: nodeA not in e and nodeB not in e
        else:
            filterFunction = lambda e: e[0] != nodeA and e[1] != nodeB
        self.edges = list(filter(filterFunction, self.edges))
        

if __name__ == "__main__":
    graph = Graph()
    
    a = GraphNode(5)
    b = GraphNode(20)
    c = GraphNode(15)
    d = GraphNode(9)
    
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