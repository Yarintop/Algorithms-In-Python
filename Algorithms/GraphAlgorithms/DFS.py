def DFS(start, target, getNeighborsFunction, explored = [], parents = {}):
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
    explored.append(start)
    neighbors = getNeighborsFunction(start)
    for n in neighbors:
        if n not in explored:
            parents[n] = start
            if n == target:
                path = []
                while n in parents:
                    path.insert(0, parents[n])
                    n = parents[n]
                return path
            return DFS(n, target, getNeighborsFunction, explored, parents)
        
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
            path = []
            while parents[v] != None:
                path.insert(0, parents[v])
                v = parents[v]
            return (v, path)
        explored.append(v)
        neighbors = getNeighborsFunction(v)
        for n in neighbors:
            if n not in explored:
                s.insert(0, n) # In BFS we append, here we insert at index 0 (BFS uses a queue, DFS uses a stack).
                explored.append(s)
                parents[n] = v
    return None
    