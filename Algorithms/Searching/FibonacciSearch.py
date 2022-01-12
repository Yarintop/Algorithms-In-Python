class FibonacciSearch:
    @staticmethod
    def fibonacciSearch(arr, x):
        """
            Given a sorted array, similar to Binary Search, Fibonacci Search divided the array to uneven parts (based on the, you guessed it, fibonacci sequence).

        Args:
            arr ((Comparable) Object Array): A sorted array containing comparable objects.
            x (Wanted Elemenet): An object the can be compared with arr's elements.

        Returns:
            Int: Returns the index of the wanted element. If it's not in the array, returns -1.
            
        Time Complexity:
            O(log(n))
        """
        a2 = 0
        a1 = 1
        an = a1 + a2
        
        while an < len(arr):
            a2 = a1
            a1 = an
            an = a1 + a2
        
        offset = -1
        
        while an > 1: # When an is 1, a2 would be 0.
            i = min(a2 + offset, len(arr) - 1)
            
            if arr[i] == x: # We found x.
                return i
            
            elif arr[i] < x: # x is greater than arr[i], we need to cut below a2 so we go back one sequence of fibonacci and raise the offset.
                an = a1
                a1 = a2
                a2 = an - a1
                offset = i # This offset 
            
            else: # x is less than arr[i], we need to cut above a2 so we go back two sequences of fibonacci.
                an = a2
                a1 = a1 - a2
                a2 = an - a1
            
        if a1 and arr[len(arr) - 1] == x:
            return len(arr) - 1
        
        return -1

if __name__ == "__main__":
    arr = [-98, -93, -73, -12, -4, 9, 10, 17, 18, 25, 33, 54, 57, 58, 58, 67, 75, 79, 91, 94, 100]
    print(FibonacciSearch.fibonacciSearch(arr, 100))
    