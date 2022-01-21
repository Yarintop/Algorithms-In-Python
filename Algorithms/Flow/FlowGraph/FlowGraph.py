from Algorithms.Flow.FlowGraph.FlowGraphEdge import FlowGraphEdge
from Algorithms.Flow.FlowGraph.FlowGraphNode import FlowGraphNode


class FlowGraph:
    def __init__(self) -> None:
        self.nodes = []
        self.edges = []
        
    def addNode(self, data):
        if isinstance(data, FlowGraphNode):
            node = data
        else:
            node = FlowGraphNode(data)
        self.nodes.append(node)
        
    def removeNode(self, data):
        for i, n in enumerate(self.nodes):
            if n.value == data:
                node = n
                del self.nodes[i]
                break
        else:
            return
        self.edges = [e for e in self.edges if e.start != node and e.end != node]
        
    def addEdge(self, node1, node2, capacity, flow=0):
        self.edges.append(FlowGraphEdge(node1, node2, capacity, flow))
        
    def removeEdge(self, node1, node2):
        self.edges = [e for e in self.edges if e.start != node1 and e.end != node2]
        
    def getEdge(self, node1, node2):
        for e in self.edges:
            if e.start == node1 and e.end == node2:
                return e
        return None