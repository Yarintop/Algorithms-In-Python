from DataStructures.Graphs.Graph.Graph import Graph
from DataStructures.Queues.PriorityQueue.PriorityQueue import PriorityQueue

from copy import deepcopy
import random

class Prim:
    @staticmethod
    def prim(graph):
        """
            Kruskal's Algorithm:
                Given a connected and undirected graph, a spanning tree of that graph is a subgraph that is a tree and connects all the vertices together.
                A single graph can have many different spanning trees. A minimum spanning tree (MST) or minimum weight spanning tree
                for a weighted, connected, undirected graph is a spanning tree with a weight less than or equal to the weight of every other spanning tree.
                The weight of a spanning tree is the sum of weights given to each edge of the spanning tree.
                
                Prim's algorithms is a greedy algorithm in which we start with a random node and choose the edge with the smallest edge that's connected to it.
                we then add the node the edge is connecting and add all of its edges to our queue and repeat until we have a minimum spanning tree.

        Args:
            graph (Graph): The graph we're trying to create an MST from.

        Returns:
            Graph: An MST of graph.
        """
        minimumSpanTree = Graph()
        numOfNodes = len(graph.nodes)
        if numOfNodes == 0:
            return minimumSpanTree
        
        nodes = [graph.nodes[0]]
        MSTEdges = []
        edgesQueue = PriorityQueue()
        for e in graph.getEdges(nodes[0]):
            edgesQueue.push(e)
            
        while len(nodes) < len(graph.nodes):
            if len(edgesQueue) == 0:
                raise ValueError("Tree must be connected.")
            e = edgesQueue.get()
            MSTEdges.append(e)
            nodeA, nodeB = e.getNodes()
            if nodeA in nodes:
                targetNode = nodeB
            else:
                targetNode = nodeA
            newEdges = []
            for edge in graph.getEdges(targetNode):
                if not any(x in nodes for x in edge.getNodes()):
                    newEdges.append(edge)
            nodes.append(targetNode)
            for newEdge in newEdges:
                edgesQueue.push(newEdge)
        
        for n in nodes:
            minimumSpanTree.addNode(n)
            
        for e in MSTEdges:
            minimumSpanTree.addEdge(e.start, e.end, e.weight)
            
        return minimumSpanTree
    
if __name__ == "__main__":
    g = Graph()
    for i in range(0, 11):
        g.addNode(i)
        
    for i in range(11):
        for j in range(i + 1, 11):
            g.addEdge(g.nodes[i], g.nodes[j], weight=random.randint(1, 100))
            
    MST = Prim.prim(g)
    
    print(sorted([x.weight for x in g.edges]))
    print(sorted([x.weight for x in MST.edges]))