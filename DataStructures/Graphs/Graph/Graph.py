from DataStructures.Graphs.Graph.GraphNode import GraphNode
from DataStructures.Graphs.Graph.GraphEdge import GraphEdge


class Graph:
    def __init__(self) -> None:
        self.nodes = []
        self.edges = []

    def adjacent(self, nodeA, nodeB):
        return any(nodeA == e.start and nodeB == e.end for e in self.edges)

    def neighbors(self, node):
        neighbors = []
        nodeEdges = [e for e in self.edges if node in e.getNodes()]
        for e in nodeEdges:
            if node == e.start:
                neighbors.append(e.end)
                
        return list(set(neighbors))
    

    def addNode(self, node):
        if node not in self.nodes:
            self.nodes.append(node)

    def removeNode(self, node):
        self.nodes.remove(node)
        self.edges = list(filter(lambda e: node not in e.getNodes(), self.edges))

    def addEdge(self, nodeA, nodeB, weight=-1, directional=False):
        self.edges = [edge for edge in self.edges if edge.start != nodeA or edge.end != nodeB]
        self.edges.append(GraphEdge(nodeA, nodeB, weight=weight))
        if not directional:
            self.edges = [edge for edge in self.edges if edge.start != nodeB or edge.end != nodeA]
            self.edges.append(GraphEdge(nodeB, nodeA, weight=weight))
        
    def getEdges(self, node):
        return [e for e in self.edges if e.start == node]

    def removeEdge(self, nodeA, nodeB, directional=False):
        if not directional:
            filterFunction = lambda e: not (nodeA in e.getNodes() and nodeB in e.getNodes())
        else:
            filterFunction = lambda e: e.start != nodeA and e.end != nodeB
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
    
    graph.removeEdge(b, d)
    
    print(graph.nodes)
    
    g2 = Graph()
    g2.addNode(a)
    g2.addNode(b)
    g2.addEdge(a, b, True)
    print(g2.adjacent(a,b))
    print(g2.adjacent(b,a))
    