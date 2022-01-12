from DataStructures.Graphs.Graph.Graph import Graph

class TopologicalSorting:
    @staticmethod
    def topologicalSorting(graph: Graph):
        l = []
        s = graph.nodes
        edges = graph.edges
        badNodes = set()
        for e in edges:
            if not e.directional:
                raise ValueError("All edges must be directional as Topological Sort only works for graphs with no cycles.")
            nodes = e.getNodes()
            badNodes.add(nodes[1])
                
        s = [x for x in s if x not in badNodes]
        
        while len(s) > 0:
            v = s.pop(0)
            l.append(v)
            for n in graph.neighbors(v):
                edges = [e for e in edges if (v, n) != e.getNodes()]
                if not any(n == e.getNodes()[1] for e in edges):
                    s.append(n)
        
        if len(edges) > 0:
            raise ValueError("Graph has at least one cycle.")
        return l
    
if __name__ == "__main__":
    g = Graph()
    g.addNode("Math 1")
    g.addNode("Math 2")
    g.addNode("Math 3")
    g.addNode("English")
    g.addNode("Physics")
    g.addNode("Physics 2")
    
    g.addEdge("Math 1", "Math 2", directional=True)
    g.addEdge("Math 1", "Math 3", directional=True)
    g.addEdge("Math 2", "Math 3", directional=True)
    g.addEdge("Physics", "Physics 2", directional=True)
    
    print(TopologicalSorting.topologicalSorting(g))
    
    