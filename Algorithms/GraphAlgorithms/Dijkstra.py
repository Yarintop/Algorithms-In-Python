from DataStructures.Graphs.Graph.Graph import Graph
from DataStructures.Graphs.Graph.GraphNode import GraphNode
from DataStructures.Queues.PriorityQueue.PriorityQueue import PriorityQueue

class Dijkstra:
    @staticmethod
    def dijkstra(graph, start, target):
        """
            Dijkstra's Algorithm finds the shortest path to a node, but unlike BFS, it's not searching by number of edges, it's searching by weights.
            
            Let the node at which we are starting be called the initial node.
            Let the distance of node Y be the distance from the initial node to Y.
            Dijkstra's algorithm will initially start with infinite distances and will try to improve them step by step.

            1.  Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
            
            2.  Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes.
                The tentative distance of a node v is the length of the shortest path discovered so far between the node v and the starting node.
                Since initially no path is known to any other vertex than the source itself (which is a path of length zero),
                all other tentative distances are initially set to infinity. Set the initial node as current.
                
            3.  For the current node, consider all of its unvisited neighbors and calculate their tentative distances through the current node.
                Compare the newly calculated tentative distance to the current assigned value and assign the smaller one.
                For example, if the current node A is marked with a distance of 6, and the edge connecting it with a neighbor B has length 2,
                then the distance to B through A will be 6 + 2 = 8. If B was previously marked with a distance greater than 8 then change it to 8.
                Otherwise, the current value will be kept.
                
            4.  When we are done considering all of the unvisited neighbors of the current node,
                mark the current node as visited and remove it from the unvisited set. A visited node will never be checked again.
            
            5.  If the destination node has been marked visited (when planning a route between two specific nodes)
                or if the smallest tentative distance among the nodes in the unvisited set is infinity
                (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes),then stop.
                The algorithm has finished.
                
            6.  Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new current node, and go back to step 3.
            
            Source: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

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
        
        start.g = 0
        pq.push(start)
        
        while len(pq) > 0:
            node = pq.get()
            if node == target:
                for d in dirty:
                    d.g = -1
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
                    if n.g > node.g + w:
                        n.g = node.g + w # update
                        parents[n] = node
                        Dijkstra.updatePriorityQueue(pq, n, n.g)
                else:
                    dirty.append(n)
                    grays.append(n)
                    n.g = node.g + w
                    parents[n] = node
                    pq.push(n)
        return None
    
    @staticmethod
    def updatePriorityQueue(pq, node, newPriority):
        temp = PriorityQueue()
        currNode = pq.get()
        while currNode != node:
            temp.push(currNode)
            currNode = pq.get()
        currNode.g = newPriority
        pq.push(currNode)
        while len(temp):
            pq.push(temp.get())

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
    
    print(Dijkstra.dijkstra(graph, nodes[4], nodes[28]) == [nodes[4], nodes[7], nodes[28]])
    print(Dijkstra.dijkstra(graph, nodes[1], nodes[9]) == [nodes[1], nodes[12], nodes[2], nodes[11], nodes[3], nodes[10], nodes[4], nodes[9]])
    