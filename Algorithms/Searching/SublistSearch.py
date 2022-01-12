from DataStructures.LinkedList.SinglyLinkedList.SinglyLinkedList import SinglyLinkedList

class SublistSearch:
    @staticmethod
    def SublistSearch(linkedList1: SinglyLinkedList, linkedList2: SinglyLinkedList):
        """
            Given two linked lists, check if linkedList2 is a sublist of linkedList1.

        Args:
            linkedList1 (SinglyLinkedList): The "parent" Linked List
            linkedList2 (SinglyLinkedList): The "Sub" Linked List

        Returns:
            Bool: True if linkedList2 is a sublist of linkedList1
            
        Time Complexity:
            Worst-Case: O(N * M)
        """
        if linkedList1.isEmpty():
            return linkedList2.isEmpty()
        list1Node = linkedList1.head
        list2Node = linkedList2.head
        while list1Node:
            while list1Node.value != list2Node.value:
                if list1Node.next == None:
                    return False
                list1Node = list1Node.next
            
            for i in range(len(linkedList2)):
                if not list1Node or list1Node.value != list2Node.value:
                    break
                list1Node = list1Node.next
                list2Node = list2Node.next
            else:
                return True
            
            list2Node = linkedList2.head
        return False
            
if __name__ == "__main__":
    l1 = SinglyLinkedList()
    
    l1.append(1)
    l1.append(2)
    l1.append(1)
    l1.append(2)
    l1.append(3)
    l1.append(4)
    l1.append(7)
    
    l2 = SinglyLinkedList()
    
    l2.append(1)
    l2.append(2)
    l2.append(3)
    l2.append(4)
    
    print(SublistSearch.SublistSearch(l1, l2))
                