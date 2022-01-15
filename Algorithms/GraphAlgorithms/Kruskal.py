from DataStructures.Graphs.Graph.Graph import Graph

import random
from copy import deepcopy

class Kruskal:
    @staticmethod
    def kruskal(graph):
        """
            Kruskal's Algorithm:
                Given a connected and undirected graph, a spanning tree of that graph is a subgraph that is a tree and connects all the vertices together.
                A single graph can have many different spanning trees.A minimum spanning tree (MST) or minimum weight spanning tree
                for a weighted, connected, undirected graph is a spanning tree with a weight less than or equal to the weight of every other spanning tree.
                The weight of a spanning tree is the sum of weights given to each edge of the spanning tree.
                
                It's a greedy algorithm in which we take the edge with the lowest weight, and try to add it to our MST, if it creates a cycle,
                then it's invalid and therefore shall be skipped to the next edge. Because we have n nodes, we need n - 1 edges to connect every single node.

        Args:
            graph (Graph): The graph we're trying to create an MST from.

        Returns:
            Graph: An MST of graph.
        """
        minimumSpanTree = Graph()
        nodes: list = deepcopy(graph.nodes)
        for n in nodes:
            minimumSpanTree.addNode(n)
        numOfNodes = len(nodes)
        nodes = [[x] for x in nodes]
        edges: list = deepcopy(graph.edges)
        edges.sort()
        
        newEdges = []
        for e in edges:
            if len(newEdges) == numOfNodes - 1:
                break
            nodeA = e.start
            nodeB = e.end
            if not Kruskal.sameGraph(nodes, nodeA, nodeB):
                newEdges.append(e)
                groupA = groupB = None
                for group in nodes:
                    if nodeA in group:
                        groupA = group
                    elif nodeB in group:
                        groupB = group
                    if groupA and groupB:
                        break
                groupA += groupB
                nodes.remove(groupB)
        
        for e in newEdges:
            minimumSpanTree.addEdge(e.start, e.end, weight=e.weight, directional=e.directional)
            
        return minimumSpanTree
        
    @staticmethod
    def sameGraph(nodes, nodeA, nodeB):
        return any(nodeA in group and nodeB in group for group in nodes)
        
if __name__ == "__main__":
    g = Graph()
    for i in range(0, 11):
        g.addNode(i)
        
    for i in range(11):
        for j in range(i, 11):
            g.addEdge(g.nodes[i], g.nodes[j], weight=random.randint(1, 100))
            
    MST = Kruskal.kruskal(g)
    
    print(sorted([x.weight for x in g.edges]))
    print(sorted([x.weight for x in MST.edges]))
    