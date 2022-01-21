class FlowGraphEdge:
    def __init__(self, s, t, capacity, flow=0) -> None:
        self.s = s
        self.t = t
        self.capacity = capacity
        self.flow = flow
        
    def addFlow(self, flow):
        if self.flow + flow > self.capacity:
            raise ValueError("Flow can't be greater than capacity.")
        self.flow += flow
        