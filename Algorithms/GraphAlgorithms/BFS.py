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
    explored = [start]
    parents = {}
    parents[start] = None
    while len(q) > 0:
        v = q.pop(0)
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
                q.append(n) # In DFS we insert at index 0, here we append (BFS uses a queue, DFS uses a stack).
                explored.append(q)
                parents[n] = v
    return None
                