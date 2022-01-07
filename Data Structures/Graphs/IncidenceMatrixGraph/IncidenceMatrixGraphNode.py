class IncidenceMatrixGraphNode:
    def __init__(self, value = None, index = -1) -> None:
        self.value = value
        self.index = index
        
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return self.__str__()