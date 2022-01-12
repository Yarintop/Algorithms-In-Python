from DataStructures.Graphs.Graph.Graph import Graph
from DataStructures.Graphs.Graph.GraphNode import GraphNode

def BFS(start, target, getNeighborsFunction):
    """
        Breadth First Search Algorithm, it starts at the root node (the start node) and searches all of its neighbors.
        If a neighbor is the target node, we return the shortest path from start to target.
        Otherwise we repeat this proccess for each neighbor until we find the target node.

    Args:
        start (Graph Node): The node we start searching from.
        target (Graph Node): The target we're searching.
        getNeighborsFunction (Function): A function we can use to find a node's neighbors (in order for this method to work on multiple data structures).

    Returns:
        Graph Node: The shortest path from the start node to the target node.
    
    Time Complexity:
        Worst-Case: O(V + E)
    """
    q = [start]
    explored = []
    parents = {}
    parents[start] = None
    while len(q) > 0:
        v = q.pop(0)
        if v == target:
            path = [v]
            while parents[v] != None:
                path.insert(0, parents[v])
                v = parents[v]
            return path
        explored.append(v)
        neighbors = getNeighborsFunction(v)
        for n in neighbors:
            if n not in explored:
                q.append(n) # In DFS we insert at index 0, here we append (BFS uses a queue, DFS uses a stack).
                explored.append(n)
                parents[n] = v
    return None
                
if __name__ == "__main__":
    graph = Graph()
    nodes = []
    
    nodes.append(GraphNode(0))
    graph.addNode(nodes[0])
    
    for i in range(1, 30):
        nodes.append(GraphNode(i))
        graph.addNode(nodes[i])
        graph.addEdge(nodes[i - 1], nodes[i])
        
    graph.addEdge(nodes[10], nodes[12])
    graph.addEdge(nodes[4], nodes[7])
    graph.addEdge(nodes[26], nodes[23])
    graph.addEdge(nodes[1], nodes[17])
    graph.addEdge(nodes[7], nodes[5])
    graph.addEdge(nodes[9], nodes[27])
    graph.addEdge(nodes[16], nodes[8])
    graph.addEdge(nodes[24], nodes[16])
    graph.addEdge(nodes[7], nodes[28])
    graph.addEdge(nodes[4], nodes[5])
    
    print(BFS(nodes[13], nodes[15], graph.neighbors) == [nodes[13], nodes[14], nodes[15]])
    print(BFS(nodes[7], nodes[2], graph.neighbors) == [nodes[7], nodes[4], nodes[3], nodes[2]])
    