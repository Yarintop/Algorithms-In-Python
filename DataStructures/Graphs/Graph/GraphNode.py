class GraphNode:
    def __init__(self, value=None) -> None:
        self.value = value
        self.g = -1
        self.f = -1
        
    def __lt__(self, other):
        if self.f == -1 and other.f == -1:
            if self.g == -1:
                return True
            return self.g < other.g
        if self.f == -1:
            return True
        return self.f < other.g
    
    def __hash__ (self):
        return id(self)
        
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return self.__str__()
    