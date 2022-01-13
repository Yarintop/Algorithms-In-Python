class SelfOrganizingListNode:
    def __init__(self, value, next=None, count=0) -> None:
        self.value = value
        self.next = next
        self.count = count
        
    def __str__(self):
        return f'{self.value}, count: {self.count}'
    
    def __repr__(self) -> str:
        return self.__str__()