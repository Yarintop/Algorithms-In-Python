from DataStructures.Graphs.Graph.Graph import Graph
from DataStructures.Graphs.Graph.GraphNode import GraphNode
from DataStructures.Queues.PriorityQueue.PriorityQueue import PriorityQueue

class AStar:
    @staticmethod
    def aStar(graph, start, target):
        """
            A* is an informed search algorithm, or a best-first search, meaning that it is formulated in terms of weighted graphs:
            starting from a specific starting node of a graph,
            it aims to find a path to the given goal node having the smallest cost (least distance travelled, shortest time, etc.).
            It does this by maintaining a tree of paths originating at the start node and extending those paths one edge at a time until
            its termination criterion is satisfied.

            At each iteration of its main loop, A* needs to determine which of its paths to extend.
            It does so based on the cost of the path and an estimate of the cost required to extend the path all the way to the goal.
            Specifically, A* selects the path that minimizes

            f(n) = g(n) + h(n)
            where n is the next node on the path, g(n) is the cost of the path from the start node to n,
            and h(n) is a heuristic function that estimates the cost of the cheapest path from n to the goal.
            A* terminates when the path it chooses to extend is a path from start to goal or if there are no paths eligible to be extended.
            The heuristic function is problem-specific. If the heuristic function is admissible,
            meaning that it never overestimates the actual cost to get to the goal, A* is guaranteed to return a least-cost path from start to goal.
            
            Note:
                Dijkstra is a special case of A* where the Heuristic Function = 0.
                As far as I knoe, Waze uses A* in their GPS app with the Heuristic Function calculating the Aerial Distance of two points
                (which is a good assumption for the actual Manhattan Distance)
            
            Source: https://en.wikipedia.org/wiki/A*_search_algorithm

        Args:
            graph (Graph): The graph we're searching in.
            start (GraphNode): The node we're starting the search from.
            target (GraphNode): The node we're searching the shortest path to.

        Returns:
            list[GraphNode]: The path from start to target.
        """
        pq = PriorityQueue()
        dirty = [start]
        blacks = []
        grays = []
        
        parents = {start: None}
        
        start.g = start.f = 0
        pq.push(start)
        
        while len(pq) > 0:
            node = pq.get()
            if node == target:
                for d in dirty:
                    d.g = -1
                    d.f = -1
                path = []
                while node:
                    path.insert(0, node)
                    node = parents[node]
                return path
            blacks.append(node)
            edges = graph.getEdges(node)
            for edge in edges:
                w = edge.weight
                n = edge.end
                if n in blacks:
                    continue
                elif n in grays:
                    if n.f > node.g + w + AStar.heuristicFunction(n, target):
                        n.g = node.g + w
                        n.f = node.g + w + AStar.heuristicFunction(n, target)
                        parents[n] = node
                        AStar.updatePriorityQueue(pq, n, node.g, w, AStar.heuristicFunction(n, target))
                else:
                    dirty.append(n)
                    grays.append(n)
                    n.g = node.g + w
                    n.f = node.g + w + AStar.heuristicFunction(n, target)
                    parents[n] = node
                    pq.push(n)
        return None
    
    @staticmethod
    def updatePriorityQueue(pq, node, g, w, h):
        temp = PriorityQueue()
        currNode = pq.get()
        while currNode != node:
            temp.push(currNode)
            currNode = pq.get()
        currNode.g = g + w
        currNode.f = g + w + h
        pq.push(currNode)
        while len(temp):
            pq.push(temp.get())
            
    @staticmethod
    def heuristicFunction(currNode, targetNode): 
        """
            This can be any function, it depends on the graph, its contents and the developer's predetermined information about them.
            In this case we know that every node have its index's value, so I'll add abs(target's index - currNode index)

        Args:
            currNode ([type]): [description]
            targetNode ([type]): [description]
        """
        return abs(currNode.value - targetNode.value)
        
if __name__ == "__main__":
    graph = Graph()
    nodes = []
    
    nodes.append(GraphNode(0))
    graph.addNode(nodes[0])
    
    for i in range(1, 30):
        nodes.append(GraphNode(i))
        graph.addNode(nodes[i])
        graph.addEdge(nodes[i - 1], nodes[i], weight=1000)
        
    graph.addEdge(nodes[1], nodes[17], weight=100)
    graph.addEdge(nodes[4], nodes[5], weight=100)
    graph.addEdge(nodes[4], nodes[7], weight=100)
    graph.addEdge(nodes[7], nodes[5], weight=100)
    graph.addEdge(nodes[7], nodes[28], weight=100)
    graph.addEdge(nodes[9], nodes[27], weight=100)
    graph.addEdge(nodes[10], nodes[12], weight=100)
    graph.addEdge(nodes[16], nodes[8], weight=100)
    graph.addEdge(nodes[24], nodes[16], weight=100)
    graph.addEdge(nodes[26], nodes[23], weight=100)
    
    graph.addEdge(nodes[1], nodes[12], weight=1)
    graph.addEdge(nodes[2], nodes[11], weight=1)
    graph.addEdge(nodes[3], nodes[10], weight=1)
    graph.addEdge(nodes[4], nodes[9], weight=1)
    graph.addEdge(nodes[10], nodes[4], weight=1)
    graph.addEdge(nodes[11], nodes[3], weight=1)
    graph.addEdge(nodes[12], nodes[2], weight=1)
    
    print(AStar.aStar(graph, nodes[4], nodes[28]) == [nodes[4], nodes[7], nodes[28]])
    print(AStar.aStar(graph, nodes[1], nodes[9]) == [nodes[1], nodes[12], nodes[2], nodes[11], nodes[3], nodes[10], nodes[4], nodes[9]])
    