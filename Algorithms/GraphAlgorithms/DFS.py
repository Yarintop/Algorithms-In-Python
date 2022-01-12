from DataStructures.Graphs.Graph.Graph import Graph
from DataStructures.Graphs.Graph.GraphNode import GraphNode

import random

class DFS:
    @staticmethod
    def DFS(start, target, getNeighborsFunction, explored = None, parents = None):
        """
            Depth First Search Algorithm, it starts at the root node (the start node) and searches one of its random neighbors.
            If a neighbor is the target node, we return the shortest path from start to target.
            Otherwise we repeat this proccess for each neighbor until we find the target node.
            If start has no unexplored neighbors we go back until we find a node with unexplored neighbors and continue from there.

            Args:
                start (Graph Node): The node we start searching from.
                target (Graph Node): The target we're searching.
                getNeighborsFunction (Function): A function we can use to find a node's neighbors (in order for this method to work on multiple data structures).

            Returns:
                Graph Node: A path (doesn't have to be the shortest) from the start node to the target node.
            
            Time Complexity:
                Worst-Case: O(V + E)
        """
        if explored == None:
            explored = []
        if parents == None:
            parents = {}
        explored.append(start)
        neighbors = getNeighborsFunction(start)
        random.shuffle(neighbors)
        for n in neighbors:
            if n not in explored:
                parents[n] = start
                if n == target:
                    path = [n]
                    while n in parents:
                        path.insert(0, parents[n])
                        n = parents[n]
                    explored = []
                    parents = {}
                    return path
                res = DFS.DFS(n, target, getNeighborsFunction, explored, parents)
                if res:
                    return res
        return None
        
    @staticmethod
    def DFS_iterative(start, target, getNeighborsFunction):
        """Same as regular DFS, but not recursive.

        Args:
            start (Graph Node): The node we start searching from.
            target (Graph Node): The target we're searching.
            getNeighborsFunction (Function): A function we can use to find a node's neighbors (in order for this method to work on multiple data structures).

        Returns:
            Graph Node: A path (doesn't have to be the shortest) from the start node to the target node.
            
        Time Complexity:
                Worst-Case: O(V + E)
        """
        s = [start]
        explored = [start]
        parents = {}
        parents[start] = None
        while len(s) > 0:
            v = s.pop(0)
            if v == target:
                path = [v]
                while parents[v] != None:
                    path.insert(0, parents[v])
                    v = parents[v]
                return path
            explored.append(v)
            neighbors = getNeighborsFunction(v)
            random.shuffle(neighbors)
            for n in neighbors:
                if n not in explored:
                    s.insert(0, n) # In BFS we append, here we insert at index 0 (BFS uses a queue, DFS uses a stack).
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
    
    print(DFS.DFS(nodes[13], nodes[15], graph.neighbors))
    print(DFS.DFS_iterative(nodes[13], nodes[15], graph.neighbors))
    print(DFS.DFS(nodes[7], nodes[2], graph.neighbors))
    print(DFS.DFS_iterative(nodes[7], nodes[2], graph.neighbors))
    