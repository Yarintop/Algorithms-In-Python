class AdjacencyListGraphNode:
    def __init__(self, value=None) -> None:
        self.value = value
        self.neighbors = []
        
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return self.__str__()