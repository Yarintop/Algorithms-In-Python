class IncidenceMatrixGraphEdge:
    def __init__(self, index, weight=0) -> None:
        self.index = index
        self.weight = weight
        
    def __str__(self):
        return str(self.index)
    
    def __repr__(self):
        return self.__str__()