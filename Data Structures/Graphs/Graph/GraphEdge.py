class GraphEdge:
    def __init__(self, start, end, weight = -1, directional=False) -> None:
        self.start = start
        self.end = end
        self.weight = weight
        self.directional = directional
        
    def getNodes(self):
        return (self.start, self.end)