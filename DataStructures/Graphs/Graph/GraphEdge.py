class GraphEdge:
    def __init__(self, start, end, weight = 1) -> None:
        self.start = start
        self.end = end
        self.weight = weight
        
    def getNodes(self):
        return (self.start, self.end)
    
    def __lt__(self, other):
        return self.weight < other.weight